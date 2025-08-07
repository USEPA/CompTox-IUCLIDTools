import hashlib
import io
import json
from pathlib import Path
from typing import Dict, Union, get_type_hints
import re
import datetime
from lxml import etree
import uuid
import mammoth
import pandas as pd
import streamlit as st
from streamlit import components
from streamlit.components import v1
import importlib
import pydantic
import zipfile
from io import BytesIO
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
import os
import typing
import sys
import tempfile
import webbrowser
sys.path.append("entity_models")

def split_camel_case(name):
    """
    Split camel case strings into space-separated words.
    Args:
        name (str): The camel case string to split.
    Returns:
        str: The space-separated string.
    """
    parts = []
    current_word = name[0]

    for char in name[1:]:
        if char.isupper() and current_word[-1].islower():
            parts.append(current_word)
            current_word = char
        else:
            current_word += char

    parts.append(current_word)
    return " ".join(parts)


def format_oht_key(file_stem):
    """
    Create a formatted key from the file name.
    Args:
        file_stem (str): The file name stem.
    Returns:
        str: The formatted OHT key, or None if the file doesn't match the expected pattern.
    """
    if "ENDPOINT_STUDY_RECORD" in file_stem:
        prefix, name = file_stem.split("ENDPOINT_STUDY_RECORD")
    elif "FLEXIBLE_RECORD" in file_stem:
        prefix, name = file_stem.split("FLEXIBLE_RECORD")
    else:
        return None  # Skip files that don't match the expected pattern

    oht_number = prefix.strip(" - ")
    name = name.lstrip(".").split("_v")[0].split("-Nano")[0].split("_OHT")[0]
    descriptive_part = split_camel_case(name)
    return f"{oht_number}: {descriptive_part}"


def read_files_from_dir(folder_path: str) -> Dict[str, pd.DataFrame]:
    """
    Read Excel files from a directory and return a dictionary of DataFrames.
    Args:
        folder_path (str): The path to the directory containing the Excel files.
    Returns:
        Dict[str, pd.DataFrame]: A dictionary mapping file stems to their corresponding DataFrames.
    """
    folder = Path(folder_path)
    return {
        file.stem: pd.read_excel(file, sheet_name=None)
        for file in folder.glob("*.xlsx")
    }


def get_unique_column_names(excel_files: Dict[str, pd.DataFrame]) -> set:
    """
    Get unique column names from a dictionary of DataFrames.
    Args:
        excel_files (Dict[str, pd.DataFrame]): A dictionary mapping file stems to their corresponding DataFrames.
    Returns:
        set: A set of unique column names.
    """
    return {
        col for df in excel_files() for col in df[list(df.keys())[0]].columns
    }


@st.cache_data
def load_oht_files(directory_path: Path) -> dict:
    """
    Load OHT files from the specified directory path.
    Args:
        directory_path (Path): The directory path containing the OHT files.
    Returns:
        dict: A dictionary mapping OHT keys to their corresponding file paths.
    """
    oht_files = {
        format_oht_key(filename.stem): {
            "docx": str(directory_path / f"{filename.stem}.docx")
        }
        for filename in directory_path.iterdir()
        if filename.is_file() and filename.stem.startswith("OHT")
    }
    return oht_files


def initialize_session_state() -> None:
    """
    Initialize session state variables.
    """
    if "split_done" not in st.session_state:
        st.session_state.split_done = False
    if "classify_pressed" not in st.session_state:
        st.session_state.classify_pressed = False
    if "show_data_preview" not in st.session_state:
        st.session_state.show_data_preview = True


def upload_file_to_df(uploaded_file: io.BytesIO) -> pd.DataFrame:
    """
    Turn uploaded file into a DataFrame.
    Args:
        uploaded_file (io.BytesIO): The uploaded file object.
    Returns:
        Optional[pd.DataFrame]: The DataFrame created from the uploaded file, or None if no file is uploaded.
    """
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1].upper()
        if file_extension == "CSV":
            user_df = pd.read_csv(uploaded_file)
        elif file_extension == "XLSX":
            user_df = pd.read_excel(uploaded_file)
        else:
            raise ValueError(f"Unsupported file format: {file_extension}")
        return user_df
    else:
        return None


def display_data_preview(user_df: pd.DataFrame) -> None:
    """
    Display a preview of the user's DataFrame if the classify button has not been pressed.
    Args:
        user_df (pd.DataFrame): The user's DataFrame.
    """
    # if not st.session_state.classify_pressed and st.session_state.show_data_preview:
    st.dataframe(
        user_df.head(5),
        hide_index=True,
        )


def classify_data(user_df: pd.DataFrame) -> pd.DataFrame:
    """
    Classify each row based on specific keywords found within the column values and recommend an OHT class accordingly.
    Args:
        user_df (pd.DataFrame): The user's DataFrame.
    Returns:
        pd.DataFrame: The classified DataFrame with OHT class recommendations and reasoning.
    """
    st.session_state.classify_pressed = True

    oht_class_list = []
    classification_reasoning_list = []
    calculated_duration_list = []

    # Define keyword conditions for OHTs (with OR groups and AND logic)
    keyword_conditions = {
        "OHT 72: Carcinogenicity": {"and": [["cancer", "carcinogenicity"]]},
        "OHT 73: Toxicity Reproduction": {"and": [["reproduction", "reproductive", "generation"]]},
        "OHT 74: Developmental Toxicity Teratogenicity": {"and": [["developmental", "teratogenicity", "gd"]]},
        "OHT 76: Neurotoxicity": {"and": [["neurotoxicity"]]},
        "OHT 41: Short Term Tox to Fish": {"and": [["fish"], ["short-term"]]},
        "OHT 42: Long Term Tox to Fish": {"and": [["fish"]]},
        "OHT 70: Genetic Toxicity Vitro": {"and": [["vitro"]]},
        "OHT 71: Genetic Toxicity Vivo": {"and": [["vivo"]]},
        "OHT 64: Skin Irritation/Corrosion": {"and": [["skin"], ["irritation", "corrosion"]]},
        "OHT 65: Eye Irritation": {"and": [["eye"], ["irritation"]]},
        "OHT 66-1: Skin Sensitisation": {"and": [["skin"], ["sensitization", "sensitisation"]]},
        "OHT 60: Acute Toxicity Oral": {"and": [["acute"], ["oral"]]},
        "OHT 61: Acute Toxicity Inhalation": {"and": [["acute"], ["inhalation"]]},
        "OHT 62: Acute Toxicity Dermal": {"and": [["acute"], ["dermal"]]},
        "OHT 67: Repeated Dose Toxicity Oral": {"and": [["repeated", "short-term", "chronic", "subchronic",
                                                         "sub-chronic"], ["oral"]]},
        "OHT 68: Repeated Dose Toxicity Inhalation": {
            "and": [["repeated", "short-term", "chronic", "subchronic", "sub-chronic"], ["inhalation"]]},
        "OHT 69-1: Repeated Dose Toxicity Dermal": {
            "and": [["repeated", "short-term", "chronic", "subchronic", "sub-chronic"], ["dermal"]]},
        "OHT 63: Acute Toxicity Other Routes": {"and": [["acute"]]},
        "OHT 69-2: Repeated Dose Toxicity Other": {"and": [["repeated", "chronic", "subchronic", "sub-chronic"]]}
    }

    time_conversion = {
        "day": 1,
        "pnd": 1, # post natal day
        "week": 7,
        "month": 30.4,
        "year": 365.24
    }

    for index, row in user_df.iterrows():
        classification_reasoning = []
        oht_class = None

        # Search for time duration to add keywords
        long_string = " ".join([str(value) for value in row.values]).lower()
        duration_pattern = r"\b(?:\d+\.\d+|\d+)[\s-]*(?:day|pnd|week|month|year)" # Regex looks for number and time unit
        max_time = 0
        for match in re.findall(duration_pattern, long_string):
            time, unit = re.split(r"[ \-]+", match) # split by space or hypthen
            time_in_days = float(time) * time_conversion[unit] # convert into days
            if time_in_days > max_time: 
                max_time = time_in_days
        
        if max_time == 0:    # use toxval definitions to define duration
            study_duration = None
        elif max_time < 31: 
            study_duration = "short-term"
        elif max_time <= 90:
            study_duration = "subchronic"
        elif max_time > 90:
            study_duration = "chronic"
        else:
            study_duration = "not found"

        row["Calculated_Study_Duration"] = study_duration
        calculated_duration_list.append(study_duration)

        # To track keywords found across columns for each OHT
        found_keywords = {oht: [] for oht in keyword_conditions}

        # Loop over each column and check for keywords within the column value
        for col_name, value in row.items():
            if pd.isna(value):
                continue  # Skip if the value is NaN

            value = str(value).lower()  # Convert to lowercase for case-insensitive matching
            tokens = re.split(r'(?<!\w)-|[^a-zA-Z0-9-]+', value)  # Split by non-alphanumeric (not "-")

            # Check for keywords and track which are found in which columns
            for oht, condition in keyword_conditions.items():
                for group in condition["and"]:
                    # If any of the OR keywords from the group are in the tokens, we mark them as found
                    matched_keyword = next((keyword for keyword in group if keyword in tokens), None)
                    if matched_keyword:
                        found_keywords[oht].append((matched_keyword, col_name))

        # Determine the OHT class based on the found keywords
        for oht, condition in keyword_conditions.items():
            required_groups = condition["and"]
            found_groups = [group for group, col in found_keywords[oht]]

            # Check if all required groups have at least one keyword found in any of them
            if all(any(set(group).intersection([found_group]) for found_group in found_groups) for group in
                   required_groups):
                oht_class = oht
                classification_reasoning += [
                    f"Found '{group}' in column '{col}'" for group, col in found_keywords[oht]
                ]
                break  # Stop once the best match is found

        # If no match is found, assign a default "Unknown" OHT class
        if not oht_class:
            oht_class = "Unknown"
            classification_reasoning.append("No matching criteria found in any columns")

        # Append the results to the lists
        oht_class_list.append(oht_class)
        classification_reasoning_list.append("; ".join(classification_reasoning))

    # Add the classification columns to the DataFrame
    user_df.insert(0, "Calculated_Study_Duration", calculated_duration_list)
    user_df.insert(0, "Classification_Reasoning", classification_reasoning_list)
    user_df.insert(0, "OHT_Class", oht_class_list)

    return user_df


def display_data_editor(edited_df: pd.DataFrame, oht_files: dict) -> None:
    """
    Display a data editor for the classified DataFrame.
    Args:
        edited_df (pd.DataFrame): The edited DataFrame.
        oht_files (dict): The dictionary of OHT files.
    """

    disabled_columns = [col for col in list(edited_df.columns) if col != 'OHT_Class']
    st.session_state.df1 = st.data_editor(
        edited_df,
        num_rows="dynamic",
        use_container_width=True,
        disabled=disabled_columns,
        column_config={
            "OHT_Class": st.column_config.SelectboxColumn(
                "OHT_Class",
                options=list(oht_files.keys()),
                help = 'Machine Classified OHT Class. Edit using the dropdown menu per record.',
                required=True,
            ),
            "Classification_Reasoning": st.column_config.TextColumn(
                'Classification_Reasoning',
                help = 'The reason the record was machine classified as the selected OHT.'  
                ),
            "Calculated_Study_Duration": st.column_config.TextColumn(
                'Calculated_Study_Duration',
                help = 'Calculated study duration based on reported duration time/units.'  
                ),
                
        },
    hide_index=True,
    )


def split_dataframe(edited_df: pd.DataFrame) -> None:
    """
    Split the edited DataFrame based on the 'OHT_Class' column and store the grouped DataFrames in the session state.
    Args:
        edited_df (pd.DataFrame): The edited DataFrame.
    """
    grouped_dfs = {category: df for category, df in edited_df.groupby("OHT_Class")}
    st.session_state.grouped_dfs = grouped_dfs
    st.success(f"Original data split into: {len(grouped_dfs)} dataframes.")
    for category, df in grouped_dfs.items():
        st.write(f"DataFrame for OHT_Class '{category}' has {len(df)} rows.")
    st.session_state.split_done = True


def merge_columns(modified_df: pd.DataFrame, merge_col1: str, merge_col2: str, merge_delimiter: str, new_merge_col_name: str) -> None:
    """
    Merge two columns in the modified DataFrame and create a new column with the merged values.
    Args:
        modified_df (pd.DataFrame): DataFrame copied from selected_df.
        merge_col1 (str): The name of the first column to merge.
        merge_col2 (str): The name of the second column to merge.
        new_merge_col_name (str): The name of the new column to store the merged values.
    """
    if merge_col1 and merge_col2 and new_merge_col_name:
        modified_df[new_merge_col_name] = (
            modified_df[merge_col1].astype(str)
            + merge_delimiter
            + modified_df[merge_col2].astype(str)
        )
        st.success(
            f"Columns '{merge_col1}' and '{merge_col2}' merged into '{new_merge_col_name}'"
        )
    else:
        st.error("Please select two columns and specify a new column name.")


def split_column(modified_df: pd.DataFrame, column_to_split: str, split_delimiter: str, split_maxsplit: int) -> None:
    """
    Split a column in the modified DataFrame based on a delimiter and create new columns for the split values.
    Args:
        modified_df (pd.DataFrame): DataFrame copied from selected_df.
        column_to_split (str): The name of the column to split.
        split_delimiter (str): The delimiter used to split the column values.
        split_maxsplit (int): The maximum number of splits to perform.
    """
    if column_to_split and split_delimiter:
        splits = modified_df[column_to_split].str.split(
            split_delimiter, n=split_maxsplit, expand=True
        )
        for i, new_col in enumerate(splits.columns):
            modified_df[f"{column_to_split}_split_{i+1}"] = splits[new_col]
        st.success(
            f"Column '{column_to_split}' split into {len(splits.columns)} columns"
        )
    else:
        st.error("Please select a column and specify a delimiter.")

#%%

# %%

def map_columns(modified_df: pd.DataFrame, unique_cols: set, uploaded_mappings: dict = None, field_suggestions: dict = None) -> dict:
    # # If input dataframe empty, return empty list
    # if modified_df.empty:
    #     return list()
    
    columns_to_map = list(modified_df.columns)
    columns_to_map = [col for col in columns_to_map if col not in ['OHT_Class', 'Classification_Reasoning']] 
    # columns_to_map.remove('OHT_Class')
    # columns_to_map.remove('Classification_Reasoning')

    data = [[user_col, "", "", "", ""] for user_col in columns_to_map]

    if uploaded_mappings:
        for row in data:
            user_col = row[0]
            if user_col in uploaded_mappings:
                mapped_oht_column = uploaded_mappings[user_col]
                common_field_path = ".".join(mapped_oht_column.split(".")[2:])
                matching_oht_column = None
                for oht_col in unique_cols:
                    oht_col_path = ".".join(oht_col.split(".")[2:])
                    if oht_col_path == common_field_path:
                        matching_oht_column = oht_col
                        break
                row[1] = matching_oht_column if matching_oht_column else None
                    #(uploaded_mappings)[user_col]
            else:
                row[1] = None

    if field_suggestions:
        for row in data:
            user_col = row[0]
            if user_col in field_suggestions:
                suggested_col = field_suggestions[user_col]
                row[2] = suggested_col
            else:
                row[2] = None

    df = pd.DataFrame(data, columns=["User Column", "OHT Column", "Machine Suggested Column Mapping", "Expected Value Type", "Picklist Values"])
    opt = ['', 'Picklist', 'Free Text']

    st.divider() # Horizontal divider
    st.title("Step 4: Map Columns to OHT Columns")
    st.write("**Map your columns (optionally Upload Column Mapping file):**")
    column_config = {
        "User Column": st.column_config.Column("User Column", 
                                               width='large',
                                               help='Original input column name'),
        "OHT Column": st.column_config.SelectboxColumn(
            "OHT Column",
            width="large",
            help='Select an OHT Column',
            options=list(unique_cols),
            required=False,
        ),
        "Machine Suggested Column Mapping": st.column_config.Column("Machine Suggested Column to assist with OHT Column selection", 
                                                                    width='large',
                                                                    help='Select a Machine Suggested OHT Column'),
        "Expected Value Type": st.column_config.SelectboxColumn(
            "Expected Value Type",
            width="medium",
            help='Select the expected value type for the column, if applicable',
            options=opt,
            required=False
        ),
    }
    updated_df = st.data_editor(
        df,
        num_rows="dynamic",
        use_container_width=True,
        column_config=column_config,
        key="column_mapping_data_editor",
    )

    if updated_df is not None:
        column_mapping = {}
        used_unique_cols = set()
        for index, row in updated_df.iterrows():
            user_col = row["User Column"]
            unique_col = row["OHT Column"]

            if unique_col and unique_col not in used_unique_cols:
                column_mapping[user_col] = unique_col
                used_unique_cols.add(unique_col)
            elif unique_col and unique_col in used_unique_cols:
                st.error(f"The OHT column '{unique_col}' has already been mapped. Please select another.")

    return column_mapping


def preview_column_mapping(column_mapping: dict, modified_df: pd.DataFrame) -> None:
    """
    Preview the column mapping and provide options to download the mapping and modified data.
    Args:
        column_mapping (dict): The dictionary representing the column mapping.
        modified_df (pd.DataFrame): DataFrame copied from selected_df.
    """
    mapping_json = json.dumps(column_mapping, indent=4)
    st.text_area("Column Mapping JSON:", mapping_json, height=250)
    st.download_button(
        label="Download Column Mapping",
        data=mapping_json,
        file_name="column_mapping.json",
        mime="application/json",
        icon=":material/download:"
    )
    st.download_button(
        label="Download Modified Data",
        data=modified_df.to_csv(index=False).encode("utf-8"),
        file_name="modified_data.csv",
        mime="text/csv",
        icon=":material/download:"
    )


def display_word_document(oht_docx_path: str) -> None:
    """
    Display the Word document for the selected OHT.
    Args:
        oht_docx_path (str): The path to the Word document.
    """
    # https://stackabuse.com/how-to-convert-docx-to-html-with-python-mammoth/
    # Map Docx styles to HTML
    custom_styles = """ 
                    b => b.strong
                    u => u.initialism
                    p[style-name='Heading 1'] => h1.card
                    table => table.table.table-hover
                    """
    # Custom CSS, add HTML tag for tab name default
    docx_css = '''
    <title>OHT Documentation</title>
<style>
td, tr, th {
    border: solid 2px lightgrey;
}

</style>
<table style="border: 5px solid #990000; border-collapse: collapse">
    '''
    # https://getbootstrap.com/docs/4.4/getting-started/introduction/
    bootstrap_css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">'
    bootstrap_js = '''
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    ''' 

    # with st.expander("Click to show WORD document for the OHT", icon=":material/description:"):
    with open(oht_docx_path, 'rb') as doc:
        result_html = mammoth.convert_to_html(doc, style_map = custom_styles)
        html_content = result_html.value
        edited_html = docx_css + bootstrap_css + html_content + bootstrap_js
        # st.components.v1.html(edited_html, height=600, scrolling=True)
        # TODO Discuss how to open from a temporary file between user sessions
        # Write HTML to file and open in new tab
        with open("output/oht_file.html", "w") as f:
            f.write(edited_html)

        # Open the file in a new tab
        webbrowser.open_new_tab(os.path.abspath("output/oht_file.html"))

def parse_column_name(column_name: str):
    if "ENDPOINT_STUDY_RECORD" in column_name:
        match = re.match(r'ENDPOINT_STUDY_RECORD\.(\w+)\.(.+)', column_name)
        oht_type = match.group(1)  # e.g., 'RepeatedDoseToxicity'
        field_path = match.group(2).split('.')  # e.g., ['MaterialsAndMethods', 'TestAnimals', 'Sex', 'value']
    elif "ReferenceSubstance" in column_name:
        match = re.match(r'ReferenceSubstance\.(.+)', column_name)
        oht_type = "ReferenceSubstance"  # e.g., 'RepeatedDoseToxicity'
        field_path = match.group(1).split('.')
    elif "Substance" in column_name:
        match = re.match(r'Substance\.(.+)', column_name)
        oht_type = "Substance"  # e.g., 'RepeatedDoseToxicity'
        field_path = match.group(1).split('.')  # e.g., ['MaterialsAndMethods', 'TestAnimals', 'Sex', 'value']
    elif "TestMaterialInformation" in column_name:
        match = re.match(r'TestMaterialInformation\.(.+)', column_name)
        oht_type = "TestMaterialInformation"  # e.g., 'RepeatedDoseToxicity'
        field_path = match.group(1).split('.')  # e.g., ['MaterialsAndMethods', 'TestAnimals', 'Sex', 'value']
    elif "LegalEntity" in column_name:
        match = re.match(r'LegalEntity\.(.+)', column_name)
        oht_type = "LegalEntity"  # e.g., 'RepeatedDoseToxicity'
        field_path = match.group(1).split('.')  # e.g., ['MaterialsAndMethods', 'TestAnimals', 'Sex', 'value']
    return oht_type, field_path


def camel_to_snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def snake_to_camel(name):
    return "".join([t.capitalize() for t in name.split('_')])

def to_document_type_format(oht_type):
    return "_".join(re.findall(r'[A-Z][^A-Z]*', oht_type)).upper()


def get_actual_type(field_type):
    if isinstance(field_type, typing._GenericAlias) and field_type.__origin__ is typing.Union:
        for arg in field_type.__args__:
            if arg is not type(None):  # Ignore NoneType
                return arg
    return field_type


def get_actual_type2(field_type):
    if hasattr(field_type, "__origin__") and field_type.__origin__ is Union:
        return next(t for t in field_type.__args__ if t is not type(None))
    return field_type


def generate_uuid():
    return str(uuid.uuid4())


def create_platform_metadata(instance, oht_type, main_uuid):
    docType = oht_type
    docSubType = ""
    # TODO create list of document types to exclude - add document_type param based on earlier ifelse
    if 'EndpointStudyRecord' in type(instance).__name__:
       docType = "ENDPOINT_STUDY_RECORD"
       docSubType = snake_to_camel(oht_type)
       
    return {
        "iuclidVersion": "7.0.7",
        "documentKey": f"{generate_uuid()}/{main_uuid}",
        "parentDocumentKey": "",
        "name": "",
        "documentType": docType,
        "documentSubType": docSubType,
        "orderInSectionNo": "1",
        "definitionVersion": "8.0",
        "creationDate": datetime.datetime.utcnow().isoformat() + "Z",
        "lastModificationDate": datetime.datetime.utcnow().isoformat() + "Z",
        "submissionType": "",
        "submissionTypeVersion": "",
        "submittingLegalEntity": "",
        "dossierSubject": "",
        "i5Origin": "false",
        "creationTool": "IUC6",
        "snapshotCreationTool": "IUC6"
    }


def get_oht_classes(oht_type):
    module_name = f"entity_models.{oht_type.lower()}_6_5.models"
    module = importlib.import_module(module_name)
    if oht_type == 'TestMaterialInformation':
        oht_class_name = oht_type
    elif oht_type == "ReferenceSubstance":
        oht_class_name = oht_type
    elif oht_type == 'Substance':
        oht_class_name = oht_type
    elif oht_type == 'LegalEntity':
        oht_class_name = oht_type
    else:
        oht_class_name = f"EndpointStudyRecord{oht_type}"
    oht_class = getattr(module, oht_class_name)
    nested_classes = {cls_name: getattr(module, cls_name) for cls_name in dir(module) if
                      cls_name.startswith(oht_class_name)}

    return oht_class, nested_classes


def set_nested_field(instance, field_path, value):
    current = instance
    for field in field_path[:-1]:
        field_snake_case = camel_to_snake(field)
        if not hasattr(current, field_snake_case) or getattr(current, field_snake_case) is None:
            field_type = current.__annotations__.get(field_snake_case)
            if field_type:
                actual_type = get_actual_type(field_type)
                nested_instance = actual_type()
                setattr(current, field_snake_case, nested_instance)
        current = getattr(current, field_snake_case)
    final_field_snake_case = camel_to_snake(field_path[-1])

    if hasattr(current, final_field_snake_case):
        setattr(current, final_field_snake_case, value)
    else:
        entry_field_snake_case = camel_to_snake(field_path[-2])
        if hasattr(current, entry_field_snake_case):
            entry_instance = getattr(current, entry_field_snake_case)
            if isinstance(entry_instance, list):
                for entry in entry_instance:
                    if hasattr(entry, final_field_snake_case):
                        setattr(entry, final_field_snake_case, value)
                        break
            elif hasattr(entry_instance, final_field_snake_case):
                setattr(entry_instance, final_field_snake_case, value)
        else:
            raise AttributeError(f"Attribute {final_field_snake_case} not found in {type(current)}")
    setattr(current, final_field_snake_case, value)


def create_instance_from_csv_row(oht_class, nested_classes, row_data):
    # Create an instance of the top-level class
    oht_instance = oht_class()
    for column_name, value in row_data.items():
        #st.write(value)
        if pd.isna(value) or value in [None, 'None', 'none', 'NA', 'na', '']:
            #st.write(value)
            continue
        else:
            _, field_path = parse_column_name(column_name)
            if field_path:
                set_nested_field(oht_instance, field_path, value)

    return oht_instance


def map_csv_to_oht_instances(data, test_material_uuid_map, test_material_columns, substance_uuid_map, substance_columns,
                             main_uuid):
    oht_instances = []
    #st.write(data)
    for index, row in data.iterrows():
        #st.write('start')
        first_column_name = data.columns[0]
        oht_type, _ = parse_column_name(first_column_name)
        # if not oht_type or oht_type == "TestMaterialInformation":
        #     continue
        # elif oht_type == "Substance":
        #     continue
        # elif oht_type == "LegalEntity":
        #     continue
        # elif oht_type == "ReferenceSubstance":
        #     continue
        if not oht_type:
            raise ValueError(f"Invalid column name format: {first_column_name}")

        substance_uuid = None
        endpoint_columns = [col for col in data.columns if col.startswith("ENDPOINT_STUDY_RECORD")]
        if not endpoint_columns:
            continue
        first_column_name = endpoint_columns[0]
        oht_type, _ = parse_column_name(first_column_name)
        oht_class, nested_classes = get_oht_classes(oht_type)
        endpoint_row_data = {col: row[col] for col in endpoint_columns if col in row}
        oht_instance = create_instance_from_csv_row(oht_class, nested_classes, endpoint_row_data)

        if test_material_columns:
            test_material_values = tuple(row[col] for col in test_material_columns if col in row)
            if test_material_values in test_material_uuid_map:
                test_material_uuid = test_material_uuid_map[test_material_values]
                set_nested_field(oht_instance, ['MaterialsAndMethods', 'TestMaterials', 'TestMaterialInformation'], test_material_uuid)

        if substance_columns:
            substance_values = tuple(row[col] for col in substance_columns if col in row)
            if substance_values in substance_uuid_map:
                substance_uuid = substance_uuid_map[substance_values]

        if not hasattr(oht_instance, 'uuid'):
            oht_instance.uuid = f"{generate_uuid()}/{main_uuid}"

        oht_instances.append((oht_instance, substance_uuid))
    
    return oht_instances


def create_xml_serializer(oht_type):
    # Initialize the XML context with the package containing the OHT models
    try:
        context = XmlContext(models_package=f"entity_models.{oht_type.lower()}_6_5.models")
    except Exception as e:
        print("Error in create_xml_serializer:", e)
    # Build the context recursively to include all related classes
    try:
        context.build_recursive(get_oht_classes(oht_type)[0])
    except Exception as e:
        print(f"Context build_recursive error: {e}")
    
    # Define the namespace mapping for the XML document
    ns_map = {
        None: f"http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-{oht_type}/9.0",  # Default namespace
        "i6": "http://iuclid6.echa.europa.eu/namespaces/platform-fields/v1",  # Namespace for platform fields
    }

    # Configure the XML serializer with pretty print and XML declaration settings
    config = SerializerConfig(
        pretty_print=True,  # Format the XML with indentation for readability
        xml_declaration=True,  # Include the XML declaration at the top of the document
        ignore_default_attributes=True,  # Ignore default attributes during serialization
    )

    # Create the XML serializer with the specified configuration and context
    serializer = XmlSerializer(config=config, context=context)
    return serializer, ns_map  # Return the serializer and namespace mapping


def instance_to_i6d(instance, oht_type, main_uuid, parent_key=None):
    """Convert an instance to an i6d XML file."""
    if main_uuid is None:
        return
    # Create an XML serializer and namespace mapping for the given OHT type
    serializer, ns_map = create_xml_serializer(oht_type)
    # Serialize the instance to XML
    try:
        xml_content = serializer.render(instance, ns_map)
    except Exception as e:
        print(f"xml_content error: {e}")
   
    # Remove the XML declaration from the serialized content
    xml_content = xml_content.split("?>", 1)[1].strip()
    document_type = to_document_type_format(oht_type)
    # Create platform metadata for the i6d file
    platform_metadata = create_platform_metadata(instance=instance, 
                                                 oht_type = document_type, 
                                                 main_uuid = main_uuid)
    if parent_key:
        platform_metadata['parentDocumentKey'] = f'{parent_key}/{main_uuid}'
    platform_metadata['documentKey'] = instance.uuid

    # Format the platform metadata as an XML string
    platform_metadata_xml = f"""
    <i6c:PlatformMetadata 
        xmlns:i6c="http://iuclid6.echa.europa.eu/namespaces/platform-container/v2"
        xmlns:i6m="http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1">
        <i6m:iuclidVersion>{platform_metadata['iuclidVersion']}</i6m:iuclidVersion>
        <i6m:documentKey>{platform_metadata['documentKey']}</i6m:documentKey>
        <i6m:parentDocumentKey>{platform_metadata['parentDocumentKey']}</i6m:parentDocumentKey>
        <i6m:name>{platform_metadata['name']}</i6m:name>
        <i6m:documentType>{platform_metadata['documentType']}</i6m:documentType>
        <i6m:documentSubType>{platform_metadata['documentSubType']}</i6m:documentSubType>
        <i6m:orderInSectionNo>{platform_metadata['orderInSectionNo']}</i6m:orderInSectionNo>
        <i6m:definitionVersion>{platform_metadata['definitionVersion']}</i6m:definitionVersion>
        <i6m:creationDate>{platform_metadata['creationDate']}</i6m:creationDate>
        <i6m:lastModificationDate>{platform_metadata['lastModificationDate']}</i6m:lastModificationDate>
        <i6m:submissionType>{platform_metadata['submissionType']}</i6m:submissionType>
        <i6m:submissionTypeVersion>{platform_metadata['submissionTypeVersion']}</i6m:submissionTypeVersion>
        <i6m:submittingLegalEntity>{platform_metadata['submittingLegalEntity']}</i6m:submittingLegalEntity>
        <i6m:dossierSubject>{platform_metadata['dossierSubject']}</i6m:dossierSubject>
        <i6m:i5Origin>{platform_metadata['i5Origin']}</i6m:i5Origin>
        <i6m:creationTool>{platform_metadata['creationTool']}</i6m:creationTool>
        <i6m:snapshotCreationTool>{platform_metadata['snapshotCreationTool']}</i6m:snapshotCreationTool>
    </i6c:PlatformMetadata>
    """

    # Define the namespace mapping for the entire i6d document
    ns_map = {
        None: f"http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-{oht_type}/9.0",  # Default namespace
        "i6c": "http://iuclid6.echa.europa.eu/namespaces/platform-container/v2",  # Namespace for platform container
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",  # XML Schema instance namespace,
        "xml": "http://www.w3.org/XML/1998/namespace"
    }

    # Create the root element for the i6d document with the specified namespaces
    root = etree.Element("{http://iuclid6.echa.europa.eu/namespaces/platform-container/v2}Document", nsmap=ns_map)

    # Parse the platform metadata XML string into an XML element
    platform_metadata_element = etree.fromstring(platform_metadata_xml)

    # Append the platform metadata element to the root
    root.append(platform_metadata_element)

    # Create the Content element
    content_element = etree.Element("{http://iuclid6.echa.europa.eu/namespaces/platform-container/v2}Content", nsmap=ns_map)

    # Append the serialized instance content to the Content element
    content_element.append(etree.fromstring(xml_content))

    # Append the Content element to the root
    root.append(content_element)

    # Create an XML tree from the root element
    tree = etree.ElementTree(root)
    document_key = platform_metadata['documentKey'].replace("/", "_")

    # Write the XML tree to a file
    i6d_buffer = io.BytesIO()
    tree.write(i6d_buffer, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    i6d_buffer.seek(0)

    # Write to i6z zip stored in state
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], "a", zipfile.ZIP_DEFLATED, False) as zip_file:     
        zip_file.writestr(f"{document_key}.i6d", i6d_buffer.getvalue())            
    
    return document_key


def create_manifest(i6d_files, main_uuid):
    """
    Create a manifest XML file that lists all i6d files, with general-information and contained-documents sections.
    Args:
        i6d_files (list): List of i6d file paths (full or relative).
        file_path (str): Path to write the manifest.xml.
        main_uuid (str): The main UUID to use for base-document-uuid.
    """
    NS = "http://iuclid6.echa.europa.eu/namespaces/manifest/v1"
    XLINK = "http://www.w3.org/1999/xlink"
    NSMAP = {None: NS, "xlink": XLINK}

    # Root <manifest>
    root = etree.Element(f"{{{NS}}}manifest", nsmap=NSMAP)

    # <general-information>
    general_info = etree.SubElement(root, f"{{{NS}}}general-information")
    etree.SubElement(general_info, f"{{{NS}}}title").text = "IUCLID 6 container manifest file"
    etree.SubElement(general_info, f"{{{NS}}}created").text = datetime.datetime.utcnow().isoformat() + "Z"
    etree.SubElement(general_info, f"{{{NS}}}author").text = "EZ Mapper"
    etree.SubElement(general_info, f"{{{NS}}}application").text = "IUCLID6 (EZ Mapper Export)"
    etree.SubElement(general_info, f"{{{NS}}}submission-type").text = "EXPERIMENTAL_DATA"
    etree.SubElement(general_info, f"{{{NS}}}archive-type").text = "DOSSIER_DATA"
    # TODO Add legistlations-info tags?
    legislation_list = etree.SubElement(general_info, f"{{{NS}}}legislations-info")
    legislation = etree.SubElement(legislation_list, f"{{{NS}}}legislation")
    # domain legislation
    etree.SubElement(legislation, f"{{{NS}}}id").text = "domain"
    etree.SubElement(legislation, f"{{{NS}}}version").text = "8.0"
    # core legislation
    legislation = etree.SubElement(legislation_list, f"{{{NS}}}legislation")
    etree.SubElement(legislation, f"{{{NS}}}id").text = "core"
    etree.SubElement(legislation, f"{{{NS}}}version").text = "8.0"
    # oecd legislation
    legislation = etree.SubElement(legislation_list, f"{{{NS}}}legislation")
    etree.SubElement(legislation, f"{{{NS}}}id").text = "oecd"
    etree.SubElement(legislation, f"{{{NS}}}version").text = "8.0"
    # TODO Is "partial" tag needed?
    # etree.SubElement(general_info, f"{{{NS}}}partial").text = "false"

    # <base-document-uuid>
    base_uuid = f"{main_uuid}/{main_uuid}"
    etree.SubElement(root, f"{{{NS}}}base-document-uuid").text = base_uuid

    # <contained-documents>
    contained_docs = etree.SubElement(root, f"{{{NS}}}contained-documents")

    # Loop through the i6z_io_buffer for i6d file information
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], 'r') as i6z_io_buffer:
        for filename in i6z_io_buffer.namelist():
            if filename in i6d_files:
                with i6z_io_buffer.open(filename) as i6d_file:
                    file_name = os.path.basename(i6d_file.name)
                    uuid_underscore = os.path.splitext(file_name)[0]
                    uuid_slash = uuid_underscore.replace("_", "/")
                    mod_time = datetime.datetime.utcnow().isoformat() + "Z"

                    # --- Extract documentType and documentSubType from the i6d file ---
                    try:
                        tree = etree.parse(i6d_file)
                        nsmap = {
                            "i6c": "http://iuclid6.echa.europa.eu/namespaces/platform-container/v2",
                            "i6m": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
                        }
                        doc_type = tree.findtext(".//i6m:documentType", namespaces=nsmap)
                        doc_subtype = tree.findtext(".//i6m:documentSubType", namespaces=nsmap)
                    except Exception as e:
                        doc_type = None
                        doc_subtype = None

                    doc_elem = etree.SubElement(contained_docs, f"{{{NS}}}document", id=uuid_slash)
                    # Use extracted type/subtype, fallback to "DOSSIER"/"EXPERIMENTAL_DATA"
                    etree.SubElement(doc_elem, f"{{{NS}}}type").text = doc_type if doc_type else "DOSSIER"
                    if doc_subtype and doc_subtype.strip():
                        etree.SubElement(doc_elem, f"{{{NS}}}subtype").text = doc_subtype
                    name_elem = etree.SubElement(doc_elem, f"{{{NS}}}name")
                    name_elem.text = file_name
                    name_elem.attrib[f"{{{XLINK}}}type"] = "simple"
                    name_elem.attrib[f"{{{XLINK}}}href"] = f"{uuid_underscore}.i6d"
                    etree.SubElement(doc_elem, f"{{{NS}}}first-modification-date").text = mod_time
                    etree.SubElement(doc_elem, f"{{{NS}}}last-modification-date").text = mod_time
                    etree.SubElement(doc_elem, f"{{{NS}}}uuid").text = uuid_slash

    # TODO Eventually add optional XSL stylesheet tag
    # # Prepare XSL stylesheet tag
    # stylesheet_pi = etree.ProcessingInstruction(
    #     "xml-stylesheet", 'type="text/xsl" href="manifest.xsl"'
    # )
    # # Insert the processing instruction at the beginning of the tree
    # root.addprevious(stylesheet_pi)
    
    # Write the XML tree to file
    tree = etree.ElementTree(root)

    # Write the XML tree to a file
    manifest_buffer = io.BytesIO()
    tree.write(manifest_buffer, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    manifest_buffer.seek(0)

    # Write to i6z zip stored in state
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], "a", zipfile.ZIP_DEFLATED, False) as zip_file:     
        zip_file.writestr("manifest.xml", manifest_buffer.getvalue())

def save_dataframe_as_excel(data):
    # Write the data to XLSX buffer file
    excel_buffer = io.BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name='Sheet1', index=False)
    excel_buffer.seek(0)

    # Write to i6z zip stored in state
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], "a", zipfile.ZIP_DEFLATED, False) as zip_file:     
        zip_file.writestr("data.xlsx", excel_buffer.getvalue())     

@st.cache_data
def generate_i6z(endpoint_instances, test_material_instances, legal_entity_instances, ref_sub_instances,
                 substance_instances, data, other_files, main_uuid, parent_uuid):
    """Generate an i6z file containing multiple instances."""
    i6d_files = []  # List to store the names of i6d files
    if test_material_instances is not None:
        for i, instance in enumerate(test_material_instances):
            # Determine the OHT type from the instance class name
            oht_type = type(instance).__name__.replace("TestMaterialInformation", "")
            document_key = instance_to_i6d(instance, "TestMaterialInformation", main_uuid=main_uuid, parent_key=parent_uuid)
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if legal_entity_instances is not None:
        for i, instance in enumerate(legal_entity_instances):
            document_key = instance_to_i6d(instance, "LegalEntity", main_uuid=main_uuid, parent_key=parent_uuid)
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if ref_sub_instances is not None:
        for i, instance in enumerate(ref_sub_instances):
            document_key = instance_to_i6d(instance, "ReferenceSubstance", main_uuid=main_uuid, parent_key=parent_uuid)
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if substance_instances is not None:
        for i, instance in enumerate(substance_instances):
            document_key = instance_to_i6d(instance, "Substance", main_uuid=main_uuid, parent_key=parent_uuid)
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    for i, (instance, parent_key) in enumerate(endpoint_instances):
        # Determine the OHT type from the instance class name
        oht_type = type(instance).__name__.replace("EndpointStudyRecord", "")
        document_key = instance_to_i6d(instance, oht_type, main_uuid=main_uuid, parent_key=parent_uuid)

        i6d_file_path = f"{document_key}.i6d"

        # Add the i6d file name to the list
        i6d_files.append(i6d_file_path)
    if other_files is not None:
        for attachment in other_files:
            create_i6d_for_attachment(attachment, main_uuid)

    # Create the manifest file
    create_manifest(i6d_files, main_uuid)
    # Save input file to i6z
    save_dataframe_as_excel(data)


def apply_column_mapping(column_mapping, modified_df):
    """
    Apply column mapping to a DataFrame and return the modified DataFrame.

    Args:
    column_mapping (dict): The column mapping dictionary.
    modified_df (pd.DataFrame): The DataFrame to modify.

    Returns:
    pd.DataFrame: The modified DataFrame with new column names.
    """
    # Apply the column mapping
    columns_to_keep = [col for col in modified_df.columns if col in column_mapping]
    modified_df = modified_df[columns_to_keep]
    modified_df.rename(columns=column_mapping, inplace=True)
    return modified_df


def get_test_material_columns(column_mapping):
    """
    Identify columns mapped to Test Material Information fields.

    Args:
    column_mapping (dict): The column mapping dictionary.

    Returns:
    list: List of columns mapped to Test Material Information fields.
    """
    return [oht_col for user_col, oht_col in column_mapping.items() if 'TestMaterialInformation' in oht_col]


def get_substance_columns(column_mapping):
    """
    Identify columns mapped to Test Material Information fields.

    Args:
    column_mapping (dict): The column mapping dictionary.

    Returns:
    list: List of columns mapped to Test Material Information fields.
    """
    return [oht_col for user_col, oht_col in column_mapping.items() if 'Substance' in oht_col and
            "ReferenceSubstance" not in oht_col]


def get_ref_sub_columns(column_mapping):
    """
    Identify columns mapped to Test Material Information fields.

    Args:
    column_mapping (dict): The column mapping dictionary.

    Returns:
    list: List of columns mapped to Test Material Information fields.
    """
    return [oht_col for user_col, oht_col in column_mapping.items() if 'ReferenceSubstance' in oht_col]


def get_legal_entity_columns(column_mapping):
    """
    Identify columns mapped to Test Material Information fields.

    Args:
    column_mapping (dict): The column mapping dictionary.

    Returns:
    list: List of columns mapped to Test Material Information fields.
    """
    return [oht_col for user_col, oht_col in column_mapping.items() if 'LegalEntity' in oht_col]


def save_uploaded_files(uploaded_files, output_dir):
    file_paths = []
    for uploaded_file in uploaded_files:
        file_path = os.path.join(output_dir, uploaded_file.name)
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(file_path)
    return file_paths


def create_test_material_instances(data, test_material_columns, main_uuid):
    test_material_instances = []
    test_material_uuid_map = {}

    unique_combinations = data[test_material_columns].drop_duplicates()

    for _, row in unique_combinations.iterrows():
        filtered_row = row[test_material_columns].dropna()
        test_material_instance = create_instance_from_csv_row(
            get_oht_classes("TestMaterialInformation")[0],
            {},
            filtered_row
        )
        uuid_str = f"{generate_uuid()}/{main_uuid}"
        test_material_instance.uuid = uuid_str
        test_material_instances.append(test_material_instance)
        test_material_values = tuple(row[col] for col in test_material_columns)
        test_material_uuid_map[test_material_values] = uuid_str

    return test_material_instances, test_material_uuid_map


def create_substance_instances(data, substance_columns, ref_sub_uuid_map, ref_sub_columns, main_uuid):
    substance_instances = []
    substances_uuid_map = {}

    unique_combinations = data[substance_columns].drop_duplicates()

    for _, row in unique_combinations.iterrows():
        filtered_row = row[substance_columns].dropna()
        substance_instance = create_instance_from_csv_row(
            get_oht_classes("Substance")[0],
            {},
            filtered_row
        )
        uuid_str = f"{generate_uuid()}/{main_uuid}"
        substance_instance.uuid = uuid_str
        if ref_sub_columns:
            ref_sub_values = tuple(row[col] for col in ref_sub_columns if col in row)
            if ref_sub_values in ref_sub_uuid_map:
                reference_uuid = ref_sub_uuid_map[ref_sub_values]
                substance_instance.parent_key = reference_uuid

        substance_instances.append(substance_instance)
        substance_values = tuple(row[col] for col in substance_columns)
        substances_uuid_map[substance_values] = uuid_str

    return substance_instances, substances_uuid_map


def create_legal_entity_instances(data, legal_entity_columns, main_uuid):
    legal_entity_instances = []
    legal_entity_uuid_map = {}

    unique_combinations = data[legal_entity_columns].drop_duplicates()

    for _, row in unique_combinations.iterrows():
        filtered_row = row[legal_entity_columns].dropna()
        legal_entity_instance = create_instance_from_csv_row(
            get_oht_classes("LegalEntity")[0],
            {},
            filtered_row
        )
        uuid_str = f"{generate_uuid()}/{main_uuid}"
        legal_entity_instance.uuid = uuid_str
        legal_entity_instances.append(legal_entity_instance)
        legal_entity_values = tuple(row[col] for col in legal_entity_columns)
        legal_entity_uuid_map[legal_entity_values] = uuid_str

    return legal_entity_instances, legal_entity_uuid_map


def create_ref_sub_instances(data, ref_sub_columns, main_uuid):
    ref_sub_instances = []
    ref_sub_uuid_map = {}

    unique_combinations = data[ref_sub_columns].drop_duplicates()

    for _, row in unique_combinations.iterrows():
        filtered_row = row[ref_sub_columns].dropna()
        ref_sub_instance = create_instance_from_csv_row(
            get_oht_classes("ReferenceSubstance")[0],
            {},
            filtered_row
        )
        uuid_str = f"{generate_uuid()}/{main_uuid}"
        ref_sub_instance.uuid = uuid_str
        ref_sub_instances.append(ref_sub_instance)
        ref_sub_values = tuple(row[col] for col in ref_sub_columns)
        ref_sub_uuid_map[ref_sub_values] = uuid_str

    return ref_sub_instances, ref_sub_uuid_map


def update_endpoint_study_records_with_test_materials(instances, test_material_uuid_map, test_material_columns, data):
    for index, instance in enumerate(instances):
        test_material_values = tuple(data.loc[index, col] for col in test_material_columns)
        if test_material_values in test_material_uuid_map:
            test_material_uuid = test_material_uuid_map[test_material_values]
            set_nested_field(instance, ['MaterialsAndMethods', 'TestMaterials', 'TestMaterialInformation'], test_material_uuid)
    return instances


def get_model_fields(model, prefix=""):
    fields = []
    for field_name, field_type in model.__annotations__.items():
        full_path = f"{prefix}.{field_name}" if prefix else field_name
        actual_type = get_actual_type2(field_type)
        if isinstance(actual_type, typing._GenericAlias):
            continue
        else:

            if hasattr(actual_type, "__annotations__") and hasattr(actual_type, "__name__"):
                if ("Substance" in actual_type.__name__ or "EndpointStudyRecord" in actual_type.__name__ or
                        "ReferenceSubstance" in actual_type.__name__ or
                        "TestMaterialInformation" in actual_type.__name__ or "LegalEntity" in actual_type.__name__):
                    nested_fields = get_model_fields(actual_type, full_path)
                    fields.extend(nested_fields)
                else:
                    fields.append(full_path)
            else:
                if hasattr(field_type, "__origin__") and field_type.__origin__ is list:
                    element_type = field_type.__args__[0]
                    actual_element_type = get_actual_type2(element_type)
                    if hasattr(actual_element_type, "__annotations__"):
                        if ("Substance" in getattr(actual_type, '__name__') or "EndpointStudyRecord" in getattr(actual_type, '__name__') or
                                "ReferenceSubstance" in getattr(actual_type, '__name__') or
                                "TestMaterialInformation" in getattr(actual_type, '__name__') or "LegalEntity" in getattr(actual_type, '__name__')):
                            nested_fields = get_model_fields(actual_type, full_path)
                            fields.extend(nested_fields)
                        else:
                            fields.append(full_path)
                    else:
                        fields.append(full_path)
                else:
                    fields.append(full_path)
    return fields


def load_and_introspect_models(model_names):
    unique_cols = set()
    for model_name in model_names:
        module_name = f"entity_models.{model_name.lower()}_6_5.models"
        module = importlib.import_module(module_name)
        model_class = getattr(module, model_name)
        fields = get_model_fields(model_class, model_name)
        unique_cols.update(fields)
    return unique_cols


def initialize_column_mapping_options(oht_type, general_model_names):
    # Introspect general models
    unique_cols = load_and_introspect_models(general_model_names)

    # Introspect the specific OHT model
    oht_class, _ = get_oht_classes(oht_type)
    endpoint_fields = get_model_fields(oht_class, f"ENDPOINT_STUDY_RECORD.{oht_type}")
    unique_cols.update(endpoint_fields)

    return unique_cols


def compute_mp5(file_content):
    """Compute the MD5 hash of a file's content"""
    md5_hash = hashlib.md5()
    md5_hash.update(file_content)
    return md5_hash.hexdigest()


def determine_mime_type(file_name):
    """Determine the MIME type based on the file extension"""
    file_extension = file_name.suffix
    if file_extension == ".pdf":
        return "application/pdf"
    elif file_extension == ".png":
        return "image/png"
    elif file_extension == ".jpg" or file_extension == ".jpeg":
        return "image/jpeg"
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


def create_i6d_for_attachment(attachment_file, output_dir, main_uuid):
    file_name = Path(attachment_file.name)

    file_content = attachment_file.getvalue()
    md5_hash = compute_mp5(file_content)
    mime_type = determine_mime_type(file_name)
    document_key = f"{generate_uuid()}/{main_uuid}"
    creation_date = datetime.datetime.utcnow().isoformat() + "Z"
    root = etree.Element("Attachment",
                         nsmap={
                             None: "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1",
                             "xlink": "http://www.w3.org/1999/xlink",
                             "xsi": "http://www.w3.org/2001/XMLSchema-instance"
                         }
    )

    etree.SubElement(root, 'documentKey').text = document_key
    etree.SubElement(root, "name").text = file_name.name
    etree.SubElement(root, "creationDate").text = creation_date
    etree.SubElement(root, "lastModificationDate").text = creation_date
    etree.SubElement(root, "md5").text = md5_hash
    etree.SubElement(root, "mimetype").text = mime_type

    # Get attachment path and new filename with md5 hash and same suffix
    attachment_filename = str((Path("attachments") / md5_hash).with_suffix(file_name.suffix))
    etree.SubElement(root, "content", {
        "{http://www.w3.org/1999/xlink}href": attachment_filename,
        "{http://www.w3.org/1999/xlink}type": "simple"
    })

    # Write to i6z zip stored in state
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], "a", zipfile.ZIP_DEFLATED, False) as zip_file:     
        zip_file.writestr(attachment_filename, attachment_file.getvalue())            

    document_key_clean = document_key.replace("/", "_")
    tree = etree.ElementTree(root)

    # Write the XML tree to a file
    i6d_buffer = io.BytesIO()
    tree.write(i6d_buffer, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    i6d_buffer.seek(0)

    # Write to i6z zip stored in state
    with zipfile.ZipFile(st.session_state['i6z_io_buffer'], "a", zipfile.ZIP_DEFLATED, False) as zip_file:     
        zip_file.writestr(f"{document_key_clean}.i6d", i6d_buffer.getvalue())            
