import streamlit as st
import warnings

import zipfile
import os
import shutil
import tempfile
import pandas as pd
import io

from pandas.api.types import (
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

import xml.etree.ElementTree as ET

from configs.config import config

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

def list_i6z_files(i6z_file: io.BytesIO, ):
    # Create temporty directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

        # Use i6z directory name
        file_info = []

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

        file_info_df = pd.DataFrame(file_info)
        # Return temporary directory name and file info dataframe
    return file_info_df

def generate_modified_i6z(i6z_file: io.BytesIO, rm_file_ls: list, copy_dir: str, out_i6z: str):
    """
    Extracts a mapping for input file extensions and .i6d files inside an IUCLID .i6z file.

    This Function:
    - Unzips the .i6z file into a temporary directory
    - Uses input file list and extracts their UUIDs (filenames without file extension)
    - Iterates through each .i6d file, checking if any UUID appears in the file content
    - Returns a DataFrame with matched .i6d and file pairs and their paths

    """
    # Get cross links to update manifest.xml
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(copy_dir, 
                                                                                row['Referenced File Name']), 
                                                                                axis=1)
    rm_file_ls_trun = [f.replace("attachments/", "") for f in rm_file_ls]
    cross_link_df = cross_link_df[cross_link_df['attachment_file_name'].isin(rm_file_ls_trun)]
    # Create temporty directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
    
        results = []

        # Collect file UUIDs (filenames without file extension)
        file_uuids = {
            os.path.join(root, f).replace(f'{temp_dir}\\', "").replace("\\", "/"): os.path.splitext(f)[0]
            for root, _, files in os.walk(temp_dir)
            for f in files
            # Add regex to search for file extensions in input list
            if os.path.join(root, f).replace(f'{temp_dir}\\', "").replace("\\", "/") in rm_file_ls
        }        

        for root, _, files in os.walk(temp_dir):
            for file in files:
                # See if file is referenced in i6d
                if file.endswith(".i6d"):
                    i6d_filename = os.path.relpath(os.path.join(root, file), temp_dir)
                    xml_path = os.path.join(root, file)

                    # Parse the XML file
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    for t_element in t_root.iter():
                        # print(t_element.attrib.items())
                        # Find the href attribute
                        if '{http://www.w3.org/1999/xlink}href' in t_element.attrib:
                            # If href to a removed file, update the path
                            if t_element.get("{http://www.w3.org/1999/xlink}href") in rm_file_ls:
                                # print(t_element.get("{http://www.w3.org/1999/xlink}href"))
                                href_orig = t_element.get("{http://www.w3.org/1999/xlink}href")
                                # New copy directory and with parent Referenced File Name
                                new_href = f'{copy_dir}/{i6z_file.name}/{file}/{href_orig.replace("attachments/", "")}'
                                # Update the href path
                                t_element.set('{http://www.w3.org/1999/xlink}href', new_href)
                                
                                # Append result for display
                                results.append(
                                    {
                                        "Referenced File Name": i6d_filename,
                                        # "uuid": file_uuids.get(href_orig), # list(file_uuids.keys())[list(file_uuids.values()).index(href_orig)],
                                        "File Name": os.path.basename(href_orig),
                                        "Old File Path": href_orig,
                                        "New File Path": new_href
                                    }
                                )
                elif  file == "manifest.xml":
                    # print(f"Checking manifest: {file}")
                    # TODO Handle manifest.xml updates with cross-link i6d parent directory matches
                    # Parse the XML file
                    xml_path = os.path.join(root, file)
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    for t_element in t_root.iter():
                        # print(t_element.attrib.items())
                        # Find the href attribute
                        if '{http://www.w3.org/1999/xlink}href' in t_element.attrib:
                            href_orig = t_element.get("{http://www.w3.org/1999/xlink}href").replace("attachments/", "")
                            if href_orig in cross_link_df['attachment_file_name'].tolist():
                                # print(f'Old: {href_orig}')
                                id6_file_name = cross_link_df.loc[cross_link_df['attachment_file_name'] == href_orig, 'Referenced File Name'].item()
                                # New copy directory and with parent Referenced File Name
                                new_href = f'{copy_dir}/{i6z_file.name}/{id6_file_name}/{href_orig.replace("attachments/", "")}'
                                # print(f'New: {new_href}')
                                # Update the href path
                                t_element.set('{http://www.w3.org/1999/xlink}href', new_href)

                                # Append result for display
                                results.append(
                                    {
                                        "Referenced File Name": file,
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
                    # print(f"Successfully deleted: {rm_file}")
                else:
                    print(f"File not found: {rm_file}")
            except OSError as e:
                print(f"Error deleting {rm_file}: {e}")

        # Write the new i6z
        with zipfile.ZipFile(out_i6z, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Iterate through the folder and add its contents to the zip file
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Get the relative path within the archive to avoid including the full source path
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname)

    df = pd.DataFrame(results)
    # print(df.head())
    return df

def get_file_cross_links(i6z_file: io.BytesIO):

    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
            zip_ref.extractall(temp_dir)

        results = []
        for root, _, files in os.walk(temp_dir):
            for file in files:
                # See if file is referenced in i6d
                if file.endswith(".i6d"):
                    i6d_filename = os.path.relpath(os.path.join(root, file), temp_dir)
                    xml_path = os.path.join(root, file)

                    # Parse the XML file
                    tree = ET.parse(xml_path)
                    t_root = tree.getroot()
                    for t_element in t_root.iter():
                        # print(t_element.attrib.items())
                        # Find the href attribute
                        if '{http://www.w3.org/1999/xlink}href' in t_element.attrib:
                            # Get all href attributes
                            subset_dict = {key: t_element.attrib[key] for key in t_element.attrib if "href" in key}
                            # print(subset_dict)
                            attachments_ls = [str(value) for value in subset_dict.values()]
                            attachments_ls = ", ".join(attachments_ls)
                            results.append(
                                {
                                    "Referenced File Name": os.path.basename(file),
                                    "attachment_file_name": attachments_ls.replace("attachments/", "")
                                }
                            )

    df = pd.DataFrame.from_dict(results)
    # print(df.head())
    return df                                

def copy_rm_i6z_files(i6z_file: io.BytesIO, copy_dir: str, copy_files: list):
    # Create subdirectory in input directory with i6z file name
    copy_dir = os.path.join(copy_dir, f'{i6z_file.name}')

    # Overwrite if already exists
    if os.path.exists(copy_dir):
        shutil.rmtree(copy_dir)
    os.makedirs(copy_dir, exist_ok=True)

    # Get file cross links to create subfolders
    cross_link_df = get_file_cross_links(i6z_file)
    cross_link_df['parent_path'] = cross_link_df.apply(lambda row: os.path.join(copy_dir, 
                                                                                row['Referenced File Name']), 
                                                                                axis=1)

    # print(f'Copying {len(copy_files)} files to directory: {copy_dir}')
    # Create temporty directory to extract i6z file into
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract input files
        with zipfile.ZipFile(i6z_file, "r") as zip_ref:
                zip_ref.extractall(temp_dir)
        
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_match = os.path.join(root, file).replace(f'{temp_dir}\\', "").replace("\\", "/")
                if file_match in copy_files:
                    # print(f"Trying to match: {file}")
                    # print(cross_link_df['attachment_file_name'])
                    parent_dir = cross_link_df[cross_link_df['attachment_file_name'] == file]
                    
                    # Check if file is linked in an i6d file to nest in subfolder
                    if parent_dir.empty:
                        dest_file = os.path.join(copy_dir, 
                                                 os.path.join(root, file).replace(f'{temp_dir}\\', ""))
                        # print(dest_file)
                    else:
                        # parent_dir = parent_dir['Referenced File Name'].values()
                        # print(f'Matched parent: {}')
                        # Create destination file path (use new parent path to referenced i6d file)
                        dest_file = os.path.join(parent_dir['parent_path'].item(), # copy_dir, 
                                                # os.path.join(root, 
                                                            file).replace(f'{temp_dir}\\', "")
                                                                #)
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
    if not st.session_state['i6z_file_selected']:
        # Prevent file being extracted multiple times
        st.session_state['i6z_file_selected'] = True
        st.session_state['i6z_file_df'] = list_i6z_files(uploaded_file)
    
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
    filtered_df = st.session_state['filter_dataframe_df'].iloc[df_file_rm.selection.rows]
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
        st.write(f"DataFrame has {len(st.session_state['i6z_file_df_rm'])} rows.")

        # Default folder to save removed files
        save_sel_files_dir = 'output'
        
        st.title("Save Removed Files")
        st.write("Click to prepare files for removal.")
        if st.button("Save Removed Files", icon=":material/file_copy:"):
            # print("Saving files...")
            with st.spinner("Saving removed files...", show_time=True):
                copy_rm_i6z_files(i6z_file = uploaded_file, 
                                  copy_dir = save_sel_files_dir, 
                                  copy_files = st.session_state['i6z_file_df_rm']['File Path'].tolist())
            st.session_state['i6z_file_rm_dir'] = os.path.join(save_sel_files_dir, 
                                                               f'{uploaded_file.name}')
            # Create zip folder
            # print(f"Saving zip file...{st.session_state['i6z_file_rm_dir']} to {save_sel_files_dir}")
            i6z_rm_file_zip = f'{st.session_state['i6z_file_rm_dir']}.zip'
            # Create zip file of the removed files
            shutil.make_archive(st.session_state['i6z_file_rm_dir'], 
                                'zip', 
                                st.session_state['i6z_file_rm_dir'])

            # open_file_explorer(st.session_state['i6z_file_rm_dir'])
            st.success(f'Files saved.')
        
        if os.path.isfile(f'{st.session_state['i6z_file_rm_dir']}.zip'):
            st.write("Click to download a zip file of the removed files.")
            # Download removed files
            st.download_button(
                label='Download removed files',
                icon=":material/download:",
                data=open(f'{st.session_state['i6z_file_rm_dir']}.zip', 'rb').read(),
                file_name=f'{uploaded_file.name}.zip',
                mime='application/octet-stream'
            )
            st.divider()

            i6z_out = os.path.join(save_sel_files_dir, f'{uploaded_file.name.replace(".i6z", "")}_modified.i6z')
            st.title("Export Modified i6z File")
            st.write("Click to generate the modified i6z file without the selected files.")
            st.warning("Note: This will modify the i6z files that reference the removed files and point to an external file location.")
            if st.button("Generate i6z File", icon=":material/manufacturing:"):
                st.success('Modified i6z Generated. Use the table below to check that the removed files listed are correct and the "New File Path" is correct.')
                st.dataframe(
                    generate_modified_i6z(i6z_file = uploaded_file, 
                                          rm_file_ls = st.session_state['i6z_file_df_rm']['File Path'].tolist(),
                                          # Set as the standard output directory parent folder where
                                          # file will ultimately be stored
                                          copy_dir = st.session_state['i6z_removed_file_final_parent_dir'].replace("\\", "/"), # save_sel_files_dir.replace("\\", "/"),
                                          out_i6z = i6z_out),
                                          column_config = {
                                              "Referenced File Name": st.column_config.Column("Referenced File Name"),
                                              "File Name": st.column_config.Column("File Name"),
                                              "Old File Path": st.column_config.Column("Old File Path", help = "Relative path within the i6z file to the file"),
                                              "New File Path": st.column_config.Column("New File Path", help = "Abolute path to where the removed file will be stored"),
                                            },
                                            use_container_width=True,
                                            hide_index=True
                )
            
                if os.path.isfile(i6z_out):
                    st.write("Click to download the modified i6z file.")
                    # Download modified i6z file
                    st.download_button(
                        label='Download modified i6z file',
                        icon=":material/download:",
                        data=open(i6z_out, 'rb').read(),
                        file_name= os.path.basename(i6z_out),
                        mime='application/octet-stream'
                    )

# TODO Handle "output" folder clean-up of intermediate files generated