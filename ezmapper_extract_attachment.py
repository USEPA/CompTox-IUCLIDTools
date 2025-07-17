import streamlit as st
import warnings
import hashlib
import zipfile
import os
import shutil
import tempfile
import pandas as pd
import io
import re
from pathlib import Path
import xml.etree.ElementTree as ET
from configs.config import config

from pandas.api.types import (
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

##################################################################################
# Utility functions to move
##################################################################################
# https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/
def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add Column Filters", key = 'filter_checkbox')

    if modify == False:
        # Set session to use for filtering
        st.session_state['filter_dataframe_df'] = df
        return df
    else:
        df = df.copy()

        # Try to convert datetimes into a standard format (datetime, no timezone)
        for col in df.columns:
            if is_object_dtype(df[col]):
                try:
                    df[col] = pd.to_datetime(df[col], format='%m/%d/%Y')
                except Exception:
                    pass

            if is_datetime64_any_dtype(df[col]):
                df[col] = df[col].dt.tz_localize(None)

        modification_container = st.container()

        with modification_container:
            to_filter_columns = st.multiselect("Filter dataframe on:", df.columns)
            for column in to_filter_columns:
                left, right = st.columns((1, 20))
                left.write("↳")
                # Treat columns with < 10 unique values as categorical
                if isinstance(df[column], pd.CategoricalDtype) or df[column].nunique() < 10:
                    user_cat_input = right.multiselect(
                        f"Values for {column}",
                        df[column].unique(),
                        default=list(df[column].unique()),
                    )
                    df = df[df[column].isin(user_cat_input)]
                elif is_numeric_dtype(df[column]):
                    _min = float(df[column].min())
                    _max = float(df[column].max())
                    step = (_max - _min) / 100
                    user_num_input = right.slider(
                        f"Values for {column}",
                        min_value=_min,
                        max_value=_max,
                        value=(_min, _max),
                        step=step,
                    )
                    df = df[df[column].between(*user_num_input)]
                elif is_datetime64_any_dtype(df[column]):
                    user_date_input = right.date_input(
                        f"Values for {column}",
                        value=(
                            df[column].min(),
                            df[column].max(),
                        ),
                    )
                    if len(user_date_input) == 2:
                        user_date_input = tuple(map(pd.to_datetime, user_date_input))
                        start_date, end_date = user_date_input
                        df = df.loc[df[column].between(start_date, end_date)]
                else:
                    user_text_input = right.text_input(
                        f"Substring or regex in {column}",
                    )
                    if user_text_input:
                        df = df[df[column].astype(str).str.contains(user_text_input)]

        # Set session to use for filtering
        st.session_state['filter_dataframe_df'] = df
        return df

def list_i6z_attachments(i6z_file: io.BytesIO):
    """
    Get list of i6z file attachments with file metadata.

    Args:
        i6z_file (io.BytesIO): Input i6z file

    Returns:
        pd.DataFrame: Dataframe of i6z attachments file details.
    """
    # Create temporty directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

        # Use i6z directory name
        file_info = []
        # Iterate through directory
        for root, _, files in os.walk(temp_dir):
                for file in files:
                    # Skip i6d, css, xsl, and manifest display to prevent users removing them
                    if file.endswith(".i6d") or file.endswith(".css") or file.endswith(".xsl") or file == "manifest.xml":
                        continue
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    _, file_ext = os.path.splitext(file)
                    file_info.append(
                        {
                            "File Name": os.path.basename(file_path),
                            "File Extension": file_ext,
                            "File Size (kb)": file_size / 1000,
                            "File Path": file_path.replace(f'{temp_dir}\\', "").replace("\\", "/"),
                        }
                    )

    return pd.DataFrame(file_info)

@st.cache_data
def generate_modified_i6z_new_path(i6z_file: io.BytesIO, rm_file_ls: list, copy_dir: str):
    """
    Generate a modified i6z file where attachment href paths are updated to new file locations.

    This Function:
    - Unzips the .i6z file into a temporary directory
    - Overwrites attachment href in manifest and i6d files to new path
    - Saves the modified .i6z file
    - Returns a DataFrame reporting the changes made

    """
    print("Generating modified i6z - new path")
    # Get cross links to update manifest.xml
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(copy_dir, 
                                                                                row['referenced_file_name']), 
                                                                                axis=1)
    # Prep to match rm_file_ls to cross_link_df filenames
    rm_file_ls_trun = [f.replace("attachments/", "") for f in rm_file_ls]
    cross_link_df = cross_link_df[cross_link_df['attachment_file_name'].isin(rm_file_ls_trun)]
    
    # Create temporty directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
    
        results = []    

        # Iterate through directory
        for root, _, files in os.walk(temp_dir):
            for file in files:
                # Modify i6d and manifest files
                if file.endswith(".i6d"):
                    i6d_filename = os.path.relpath(os.path.join(root, file), temp_dir)
                    xml_path = os.path.join(root, file)

                    # Parse the XML file
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    for t_element in t_root.iter():
                        # Find the href attribute
                        attrib_check = [key for key in t_element.attrib if '}href' in key]
                        if len(attrib_check) == 1:
                            href_attrib = attrib_check[0]
                            # If href to a removed file, update the path
                            if t_element.get(href_attrib) in rm_file_ls:
                                href_orig = t_element.get(href_attrib)
                                # New copy directory and with parent referenced_file_name
                                new_href = f'{copy_dir}/{i6z_file.name}/{file}/{href_orig.replace("attachments/", "")}'
                                # Update the href path
                                t_element.set(href_attrib, new_href)
                                # Append result for display
                                results.append(
                                    {
                                        "referenced_file_name": i6d_filename,
                                        "File Name": os.path.basename(href_orig),
                                        "Old File Path": href_orig,
                                        "New File Path": new_href
                                    }
                                )
                    # Overwrite the original XML file
                    tree.write(xml_path)
                elif  file == "manifest.xml":                    
                    # Parse the XML file
                    xml_path = os.path.join(root, file)
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    for t_element in t_root.iter():
                        # Find the href attribute
                        attrib_check = [key for key in t_element.attrib if '}href' in key]
                        if len(attrib_check) == 1:
                            href_attrib = attrib_check[0]
                            # Check if href is for a removed file
                            href_orig = t_element.get(href_attrib).replace("attachments/", "")
                            if href_orig in cross_link_df['attachment_file_name'].tolist():
                                id6_file_name = cross_link_df.loc[cross_link_df['attachment_file_name'] == href_orig, 'referenced_file_name'].item()
                                # New copy directory and with parent referenced_file_name
                                new_href = f'{copy_dir}/{i6z_file.name}/{id6_file_name}/{href_orig.replace("attachments/", "")}'
                                # Update the href path
                                t_element.set(href_attrib, new_href)
                                # Append result for display
                                results.append(
                                    {
                                        "referenced_file_name": file,
                                        # "uuid": file_uuids.get(href_orig), # list(file_uuids.keys())[list(file_uuids.values()).index(href_orig)],
                                        "File Name": os.path.basename(href_orig),
                                        "Old File Path": href_orig,
                                        "New File Path": new_href
                                    }
                                )
                    # Overwrite the original XML file
                    tree.write(xml_path)

        # Remove selected files from i6z
        for file_path in rm_file_ls:
            rm_file = os.path.join(temp_dir, file_path)
            try:
                if os.path.exists(rm_file):
                    os.remove(rm_file)
                else:
                    print(f"File not found: {rm_file}")
            except OSError as e:
                print(f"Error deleting {rm_file}: {e}")

        # Write the new i6z
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file: 
            # Iterate through the folder and add its contents to the zip file
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Get the relative path within the archive to avoid including the full source path
                    arcname = os.path.relpath(file_path, temp_dir)
                    # Read selected file
                    with open(file_path, "rb") as f:
                        file_content = f.read()
                    # Write to zip
                    zip_file.writestr(arcname, file_content)

    # Store modified i6z in session_state to serve to download later
    st.session_state['i6z_modified_zip'] = zip_buffer
    return pd.DataFrame(results)

def calculate_md5_hash(filepath):
    """
    Calculates the MD5 hash of a file's content.

    Args:
        filepath (str): Path to file to hash.

    Returns:
        str: File's MD5 hash.
    """
    hasher = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            # Read in chunks of 4096 bytes
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

@st.cache_data
def generate_modified_i6z_text_placeholder(i6z_file: io.BytesIO, rm_file_ls: list, copy_dir: str):
    """
    Generate a modified i6z file where attachment href paths, filenames, and mimetypes are updated to a text placeholder file.

    This Function:
    - Unzips the .i6z file into a temporary directory
    - Writes a placeholder text file
    - md5 hashes the placeholder text file to use as filename and in md5 tags
    - Overwrites attachment href in manifest and i6d files to the placeholder text file
    - Saves the modified .i6z file
    - Returns a DataFrame reporting the changes made

    """
    print("Generating modified i6z - text placeholder")
    # Get cross links to update manifest.xml
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(copy_dir, 
                                                                                row['referenced_file_name']), 
                                                                                axis=1)
    # Create placeholder text file string
    cross_link_df['placeholder_text'] = cross_link_df.apply(lambda row: f"File \"{row['name']}\" ({row['attachment_file_name']}) moved to \"{copy_dir}/{i6z_file.name}/{row['referenced_file_name']}/{row['attachment_file_name']}\"", axis=1)
    # Prep rm_file_ls for comparison (just the basename)
    rm_file_ls_trun = [f.replace("attachments/", "") for f in rm_file_ls]
    cross_link_df = cross_link_df[cross_link_df['attachment_file_name'].isin(rm_file_ls_trun)]

    # Create temporary directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

        # Save placeholder file to i6z temp directory
        placeholder_tmp_path = os.path.join(temp_dir, "attachments/files_moved.txt")
        cross_link_df['placeholder_text'].to_csv(placeholder_tmp_path,
                                                 index = False, header = False)
        
        # Hash and rename placeholder file
        placeholder_hash = calculate_md5_hash(placeholder_tmp_path)
        placeholder_hash_path = placeholder_tmp_path.replace("files_moved", 
                                                             placeholder_hash)
        os.rename(placeholder_tmp_path, placeholder_hash_path)
        
        results = []     

        # Iterate over files
        for root, _, files in os.walk(temp_dir):
            for file in files:
                # Modify i6d and manifest files
                if file.endswith(".i6d"):
                    # Only if i6d associated with remove file list items
                    if file in cross_link_df['referenced_file_name'].tolist():
                        print("Modifying i6d xml...")
                        i6d_filename = os.path.relpath(os.path.join(root, file), temp_dir)
                        xml_path = os.path.join(root, file)

                        # Parse the XML file
                        tree = ET.parse(xml_path)
                        t_root = tree.getroot()

                        for t_element in t_root.iter():
                            print(t_element.tag)
                            # Replace attachment file extension
                            if "}name" in t_element.tag:
                                if t_element.text is not None:
                                    p = Path(t_element.text)
                                    t_element.text = str(p.with_suffix(".txt"))
                            # Change the mimetype to text
                            elif "}mimetype" in t_element.tag:
                                t_element.text = 'text/plain'
                            # Change md5
                            elif "}md5" in t_element.tag:                                
                                t_element.text = placeholder_hash
                            
                            # Find the href attribute
                            print(t_element.attrib)
                            attrib_check = [key for key in t_element.attrib if '}href' in key]
                            if len(attrib_check) == 1:
                                href_attrib = attrib_check[0]
                                # If href to a removed file, update the path
                                href_orig = t_element.get(href_attrib)
                                print(href_orig)
                                if href_orig in rm_file_ls:                                    
                                    # New href to the placeholder text file
                                    new_href = f'attachments/{os.path.basename(placeholder_hash_path)}'
                                    # Update the href path
                                    t_element.set(href_attrib, new_href)
                                    # Append result for display
                                    results.append(
                                        {
                                            "referenced_file_name": i6d_filename,
                                            # "uuid": file_uuids.get(href_orig), # list(file_uuids.keys())[list(file_uuids.values()).index(href_orig)],
                                            "File Name": os.path.basename(href_orig),
                                            "Old File Path": href_orig,
                                            "New File Path": new_href,
                                            "Placeholder Text": cross_link_df['placeholder_text'][cross_link_df["attachment_file_name"] == os.path.basename(href_orig)].item()
                                        }
                                    )
                        # Overwrite the original XML file
                        tree.write(xml_path)
                elif  file == "manifest.xml":
                    # Parse the XML file
                    xml_path = os.path.join(root, file)
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    # Get elements that are "attachment" tags and have id that matches documentKey for remove files
                    attachment_elements = [elem for elem in t_root.findall(".//*") if elem.tag.endswith("attachment") and 
                                           elem.attrib.get('id') in cross_link_df['documentKey'].tolist()]
                    
                    # Iterate over each attachment parent element tag
                    for p_elem in attachment_elements:
                        # Iterate over child elements
                        for c_elem in p_elem:
                            # Update display filename
                            if '}name' in c_elem.tag:
                                p = Path(c_elem.text)
                                c_elem.text = str(p.with_suffix(".txt"))                                
                            # Find the href attribute
                            elif '}linked-attachments' in c_elem.tag:
                                # Iterate over child elements
                                for cc_elem in c_elem:
                                    if '}linked-doc' in cc_elem.tag:
                                        href_attrib = [key for key in cc_elem.attrib if '}href' in key][0]
                                        href_orig = cc_elem.get(href_attrib).replace("attachments/", "")
                                        if href_orig in cross_link_df['attachment_file_name'].tolist():
                                            # New href to the placeholder text file
                                            new_href = f'attachments/{os.path.basename(placeholder_hash_path)}'
                                            # Update the href path
                                            cc_elem.set(href_attrib, new_href)
                                            # Replace file extension for displayed filename
                                            p = Path(cc_elem.text)
                                            cc_elem.text = str(p.with_suffix(".txt"))
                                            # Append result for display
                                            results.append(
                                                {
                                                    "referenced_file_name": file,
                                                    "File Name": os.path.basename(href_orig),
                                                    "Old File Path": href_orig,
                                                    "New File Path": new_href,
                                                    "Placeholder Text": cross_link_df['placeholder_text'][cross_link_df["attachment_file_name"] == os.path.basename(href_orig)].item()
                                                }
                                            )
                    # Overwrite the original XML file
                    tree.write(xml_path)
        
        # Remove selected files from i6z
        for file_path in rm_file_ls:
            rm_file = os.path.join(temp_dir, file_path)
            try:
                if os.path.exists(rm_file):
                    os.remove(rm_file)
                else:
                    print(f"File not found: {rm_file}")
            except OSError as e:
                print(f"Error deleting {rm_file}: {e}")

        # Write the new i6z
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file: 
            # Iterate through the folder and add its contents to the zip file
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Get the relative path within the archive to avoid including the full source path
                    arcname = os.path.relpath(file_path, temp_dir)
                    # Read selected file
                    with open(file_path, "rb") as f:
                        file_content = f.read()
                    # Write to zip
                    zip_file.writestr(arcname, file_content)

    # Store modified i6z in session_state to serve to download later
    st.session_state['i6z_modified_zip'] = zip_buffer
    return pd.DataFrame(results)

def get_file_cross_links(i6z_file: io.BytesIO):
    """
    Get dataframe of i6z file attachments and which i6d files they link to.

    Args:
        i6z_file (io.BytesIO): Input i6z file.

    Returns:
        pd.DataFrame: Dataframe of i6z file attachments and their linked i6d files.
    """
    # Create temporary directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        results = []
        for root, _, files in os.walk(temp_dir):
            for file in files:
                # See if file is referenced in i6d
                if file.endswith(".i6d"):
                    xml_path = os.path.join(root, file)
                    # Parse the XML file
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    element_list = {"referenced_file_name": os.path.basename(file)}
                    for t_element in t_root.iter():
                        # Get all element tag text and hrefs
                        if t_element.text is not None:
                            element_list.update({re.sub(r"\{.*?\}", "", t_element.tag): t_element.text})
                        attrib_check = [key for key in t_element.attrib if '}href' in key]
                        if len(attrib_check) > 0:
                            # Get all href attributes
                            subset_dict = {key: t_element.attrib[key] for key in t_element.attrib if "href" in key}
                            attachments_ls = [str(value) for value in subset_dict.values()]
                            attachments_ls = ", ".join(attachments_ls)
                            element_list.update({"attachment_file_name": attachments_ls.replace("attachments/", "")})
                            results.append(element_list)

    return pd.DataFrame.from_dict(results)                                

@st.cache_data
def copy_rm_i6z_files_cached(i6z_file: io.BytesIO, copy_files: list):
    """
    Copy selected i6z files to a new directory.

    Args:
        i6z_file (io.BytesIO): Input i6z file.
        copy_files (list): List of i6z files to copy.
    """
    print("Generating removed i6z files zip")

    # Get file cross links to create subfolders
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(row['referenced_file_name']), 
                                                                                axis=1)

    # Create temporary directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:            
            # Iterate over files
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_match = os.path.join(root, file).replace(f'{temp_dir}\\', "").replace("\\", "/")
                    # Get matching file
                    if file_match in copy_files:
                        # Get i6z file parent
                        parent_dir = cross_link_df[cross_link_df['attachment_file_name'] == file]
                        # Check if file is linked in an i6d file to nest in subfolder
                        if parent_dir.empty:
                            dest_file = os.path.join(root, file).replace(f'{temp_dir}\\', "")
                        else:
                            # Create destination file path (use new parent path to referenced i6d file)
                            dest_file = os.path.join(parent_dir['parent_path'].item(),
                                                                file).replace(f'{temp_dir}\\', "")
                        
                        # Read selected file and write to zip
                        with open(os.path.join(root, file), "rb") as f:
                            file_content = f.read()
                        
                        zip_file.writestr(dest_file, file_content)
                        
    return zip_buffer

def copy_rm_i6z_files(i6z_file: io.BytesIO, copy_dir: str, copy_files: list):
    """
    Copy selected i6z files to a new directory.

    Args:
        i6z_file (io.BytesIO): Input i6z file.
        copy_dir (str): Parent directory path where files should be copied.
        copy_files (list): List of i6z files to copy.
    """
    # Create subdirectory in input directory with i6z file name
    copy_dir = os.path.join(copy_dir, f'{i6z_file.name}')

    # Overwrite if already exists
    if os.path.exists(copy_dir):
        shutil.rmtree(copy_dir)
    os.makedirs(copy_dir, exist_ok=True)

    # Get file cross links to create subfolders
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(copy_dir, 
                                                                                row['referenced_file_name']), 
                                                                                axis=1)

    # Create temporary directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
        # Iterate over files
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_match = os.path.join(root, file).replace(f'{temp_dir}\\', "").replace("\\", "/")
                # Get matching file
                if file_match in copy_files:
                    # Get i6z file parent
                    parent_dir = cross_link_df[cross_link_df['attachment_file_name'] == file]
                    # Check if file is linked in an i6d file to nest in subfolder
                    if parent_dir.empty:
                        dest_file = os.path.join(copy_dir, 
                                                 os.path.join(root, file).replace(f'{temp_dir}\\', ""))
                    else:
                        # Create destination file path (use new parent path to referenced i6d file)
                        dest_file = os.path.join(parent_dir['parent_path'].item(),
                                                            file).replace(f'{temp_dir}\\', "")
                    # Create subdirectories as needed
                    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                    # Copy file to new directory
                    shutil.copy(os.path.join(root, file), dest_file)

##################################################################################
# Start of App
##################################################################################
st.set_page_config(layout="wide")

# Inject JavaScript to warn on refresh or navigation
st.components.v1.html(
    """
    <script>
    window.onbeforeunload = function() {
        return "Are you sure you want to leave? Your progress will be lost.";
    };
    </script>
    """,
    height=0,
)

# Set initial state
if "i6z_file_selected" not in st.session_state:
    st.session_state['i6z_file_selected'] = False
if "i6z_file_df" not in st.session_state:
    st.session_state['i6z_file_df'] = pd.DataFrame()
if "i6z_file_df_ft" not in st.session_state:
    st.session_state['i6z_file_df_ft'] = pd.DataFrame()
if "i6z_file_df_rm" not in st.session_state:
    st.session_state['i6z_file_df_rm'] = pd.DataFrame()
if "filter_dataframe_df" not in st.session_state:
    st.session_state['filter_dataframe_df'] = pd.DataFrame()
if "i6z_file_rm_dir" not in st.session_state:
    st.session_state['i6z_file_rm_dir'] = None
if "i6z_removed_file_final_parent_dir" not in st.session_state:
    st.session_state['i6z_removed_file_final_parent_dir'] = config["i6z_removed_file_final_parent_dir"]
if "filter_checkbox" not in st.session_state:
    st.session_state['filter_checkbox'] = False
if "i6z_modified_zip" not in st.session_state:
    st.session_state['i6z_modified_zip'] = None
# Set the attachment replacement mode
if "replacement_mode" not in st.session_state:
    st.session_state['replacement_mode'] = 'text_placeholder'


# Suppress specific warnings from openpyxl that are not relevant for the user
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Create a sidebar for user inputs
st.sidebar.title("Upload File")
uploaded_file = st.sidebar.file_uploader("Choose an i6z file", type=["i6z"])

# Default uploaded_file starts as NULL
# Set the title and description of the web app
if uploaded_file is None:
    st.title("EZ Mapper")
    st.markdown("A tool for mapping and transforming data to an i6z file. **Upload** a *CSV* or *Excel* file to begin.")
    # Clear session state and stop execution if 'x' is clicked in the sidebar by the file
    st.session_state.clear()
    st.stop()
else:
    # Process the uploaded file if it exists
    st.title(f"Reviewing file: {uploaded_file.name}")
    # Check if files are selected
    if not st.session_state['i6z_file_selected']:
        # Prevent file being extracted multiple times
        st.session_state['i6z_file_selected'] = True
        st.session_state['i6z_file_df'] = list_i6z_attachments(uploaded_file)
    
    ##################################################################################
    # Filterable DataFrame File Selection
    ##################################################################################
    st.header("i6z File Contents")
    st.write("Select files to remove from the i6z file using the filters and row checkboxes.")
    # Set initial filter view state to full dataframe
    if st.session_state['i6z_file_df_ft'].empty and st.session_state['i6z_file_df_rm'].empty:
        # Only populate if user has not already selected all files for removal
        st.session_state['i6z_file_df_ft'] = st.session_state['i6z_file_df']
    elif not st.session_state['i6z_file_df_ft'].empty and not st.session_state['i6z_file_df_rm'].empty:
        st.session_state['i6z_file_df_ft'] = st.session_state['i6z_file_df'][~st.session_state['i6z_file_df']['File Path'].isin(st.session_state['i6z_file_df_rm']['File Path'])]
    
    # Display filterable dataframe
    # https://docs.streamlit.io/develop/tutorials/elements/dataframe-row-selections
    df_file_rm = st.dataframe(
        filter_dataframe(st.session_state['i6z_file_df_ft']), 
        column_config = {
            "File Name": st.column_config.Column("File Name"),
            "File Extension": st.column_config.Column("File Extension"),
            "File Size (kb)": st.column_config.Column("File Size (kb)", help = "File size in kilobytes"),
            "File Path": st.column_config.Column("File Path", help = "Relative path within the i6z file to the file"),
        },
        use_container_width=True,
        on_select="rerun",
        selection_mode = "multi-row",
        hide_index=True
    )
    # Get selected files to remove/filter out
    filtered_df = st.session_state['filter_dataframe_df'].iloc[df_file_rm.selection.rows]
    # Display counts and buttons for users to interact with for their selection
    st.write(f"DataFrame has {len(st.session_state['i6z_file_df_ft'])} rows.")
    st.write('When ready, click the "Add File Selection" button to add selected files to the "Files to Remove" table.')
    st.write('To start over, click the "Clear File Selection" button.')
    # Create buttons to Confirm or Clear row selection
    confirm_sel_col, clear_sel_col = st.columns(2)
    with confirm_sel_col:
        if st.button("Add File Selection", icon=":material/add:"):
            st.session_state['i6z_file_df_ft'] = st.session_state['i6z_file_df_ft'][~st.session_state['i6z_file_df_ft'].index.isin(df_file_rm.selection.rows)].reset_index(drop=True)
            # Append to removal df
            if st.session_state['i6z_file_df_rm'].empty:
                st.session_state['i6z_file_df_rm'] = filtered_df
            else:
                st.session_state['i6z_file_df_rm'] = pd.concat([st.session_state['i6z_file_df_rm'], filtered_df]).drop_duplicates(subset=["File Name"]).reset_index(drop=True)
            st.session_state['filter_dataframe_df'] = pd.DataFrame()
            # Force a rerun to display the updated DataFrame 
            st.rerun()
    with clear_sel_col:
        if st.button("Clear File Selection", icon=":material/cancel:"):
            st.session_state['i6z_file_df_ft'] = st.session_state['i6z_file_df']
            st.session_state['i6z_file_df_rm'] = pd.DataFrame()
            # Force a rerun to display the updated DataFrame 
            st.session_state['filter_dataframe_df'] = pd.DataFrame()
            st.rerun()

    # Display Confirmed Selected Rows
    if not st.session_state['i6z_file_df_rm'].empty:
        st.divider()
        st.header("Files to Remove")
        st.write("Review the files selected for removal.")
        # Display files to remove for user to verify
        st.dataframe(
            st.session_state['i6z_file_df_rm'],
            column_config = {
            "File Name": st.column_config.Column("File Name"),
            "File Extension": st.column_config.Column("File Extension"),
            "File Size (kb)": st.column_config.Column("File Size (kb)", help = "File size in kilobytes"),
            "File Path": st.column_config.Column("File Path", help = "Relative path within the i6z file to the file"),
            },
            use_container_width=True,
            hide_index=True
        )
        # Report counts
        st.write(f"DataFrame has {len(st.session_state['i6z_file_df_rm'])} rows.")

        # Default folder to save removed files
        save_sel_files_dir = 'output'
        
        st.title("Save Removed Files")
        
        st.write("Click to download a zip file of the removed files.")
        # Download removed files
        st.download_button(
            label='Download removed files',
            icon=":material/download:",
            data=copy_rm_i6z_files_cached(i6z_file = uploaded_file, 
                                            copy_files = st.session_state['i6z_file_df_rm']['File Path'].tolist()).getvalue(),
            file_name=f'{uploaded_file.name}.zip',
            mime='application/octet-stream',
            on_click="ignore" # Prevents rerun on click
        )
        st.divider()
        
        # Export modified i6z file 
        i6z_out = os.path.join(save_sel_files_dir, f'{uploaded_file.name.replace(".i6z", "")}_modified.i6z')
        st.title("Export Modified i6z File")
        st.write("Click to generate the modified i6z file without the selected files.")
        st.warning("Note: This will modify the i6z files that reference the removed files and point to an external file location.")
        if st.button("Generate i6z File", icon=":material/manufacturing:"):
            match st.session_state['replacement_mode']:
                case 'new_path':
                    st.success('Modified i6z Generated. Use the table below to check that the removed files listed are correct and the "New File Path" is correct.')
                    st.dataframe(
                        generate_modified_i6z_new_path(i6z_file = uploaded_file, 
                                            rm_file_ls = st.session_state['i6z_file_df_rm']['File Path'].tolist(),
                                            # Set as the standard output directory parent folder where
                                            # file will ultimately be stored
                                            copy_dir = st.session_state['i6z_removed_file_final_parent_dir'].replace("\\", "/")# , # save_sel_files_dir.replace("\\", "/"),
                                            # out_i6z = i6z_out
                                            ),
                                            column_config = {
                                                "referenced_file_name": st.column_config.Column("referenced_file_name"),
                                                "File Name": st.column_config.Column("File Name"),
                                                "Old File Path": st.column_config.Column("Old File Path", help = "Relative path within the i6z file to the file"),
                                                "New File Path": st.column_config.Column("New File Path", help = "Abolute path to where the removed file will be stored"),
                                                },
                                                use_container_width=True,
                                                hide_index=True
                    )
                case "text_placeholder":
                    st.success('Modified i6z Generated. Use the table below to check that the removed files listed are correct and the "Placeholder Text" is correct.')
                    st.dataframe(
                        generate_modified_i6z_text_placeholder(i6z_file = uploaded_file, 
                                            rm_file_ls = st.session_state['i6z_file_df_rm']['File Path'].tolist(),
                                            # Set as the standard output directory parent folder where
                                            # file will ultimately be stored
                                            copy_dir = st.session_state['i6z_removed_file_final_parent_dir'].replace("\\", "/")# , # save_sel_files_dir.replace("\\", "/"),
                                            # out_i6z = i6z_out
                                            ),
                                            column_config = {
                                                "referenced_file_name": st.column_config.Column("referenced_file_name"),
                                                "File Name": st.column_config.Column("File Name"),
                                                "Old File Path": st.column_config.Column("Old File Path", help = "Relative path within the i6z file to the file"),
                                                "New File Path": st.column_config.Column("New File Path", help = "Abolute path to where the removed file will be stored"),
                                                "Placeholder Text": st.column_config.Column("Placeholder Text", help = "Placeholder text in txt file"),
                                                },
                                                use_container_width=True,
                                                hide_index=True
                    )
                case _:
                    raise ValueError(f"Unknown replacement_mode: {st.session_state['replacement_mode']}")
            
            if st.session_state['i6z_modified_zip'] is not None:
                # User download the modified i6z file
                st.write("Click to download the modified i6z file.")
                # Download modified i6z file
                st.download_button(
                    label='Download modified i6z file',
                    icon=":material/download:",
                    data=st.session_state['i6z_modified_zip'].getvalue(),
                    file_name= os.path.basename(i6z_out),
                    mime='application/octet-stream'
                )

# TODO Handle "output" folder clean-up of intermediate files generated