import hashlib
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
import importlib
import pydantic
import zipfile
from io import BytesIO
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
import os
import typing


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
    if not st.session_state.classify_pressed and st.session_state.show_data_preview:
        st.dataframe(user_df.head(5))


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

    # Define keyword conditions for OHTs (with OR groups and AND logic)
    keyword_conditions = {
        "OHT 60: Acute Toxicity Oral": {"and": [["acute"], ["oral"]]},
        "OHT 61: Acute Toxicity Inhalation": {"and": [["acute"], ["inhalation"]]},
        "OHT 62: Acute Toxicity Dermal": {"and": [["acute"], ["dermal"]]},
        "OHT 67: Repeated Dose Toxicity Oral": {"and": [["repeated", "chronic", "subchronic"], ["oral"]]},
        "OHT 68: Repeated Dose Toxicity Inhalation": {"and": [["repeated", "chronic", "subchronic"], ["inhalation"]]},
        "OHT 69-1: Repeated Dose Toxicity Dermal": {"and": [["repeated", "chronic", "subchronic"], ["dermal"]]},
        "OHT 72: Carcinogenicity": {"and": [["cancer", "carcinogenicity"]]},
        "OHT 73: Toxicity Reproduction": {"and": [["reproduction", "reproductive"]]},
        "OHT 74: Developmental Toxicity Teratogenicity": {"and": [["developmental", "teratogenicity"]]},
        "OHT 41: Short Term Tox to Fish": {"and": [["fish"], ["short-term"]]},
        "OHT 42: Long Term Tox to Fish": {"and": [["fish"]]},
        "OHT 70: Genetic Toxicity Vitro": {"and": [["vitro"]]},
        "OHT 71: Genetic Toxicity Vivo": {"and": [["vivo"]]},
        "OHT 64: Skin Irritation/Corrosion": {"and": [["skin"], ["irritation", "corrosion"]]},
        "OHT 65: Eye Irritation": {"and": [["eye"], ["irritation"]]},
        "OHT 66-1: Skin Sensitisation": {"and": [["skin"], ["sensitization", "sensitisation"]]},
        "OHT 63: Acute Toxicity Other Routes": {"and": [["acute"]]},
        "OHT 69-2: Repeated Dose Toxicity Other": {"and": [["repeated", "chronic", "subchronic"]]}
    }

    for index, row in user_df.iterrows():
        classification_reasoning = []
        oht_class = None

        # To track keywords found across columns for each OHT
        found_keywords = {oht: [] for oht in keyword_conditions}

        # Loop over each column and check for keywords within the column value
        for col_name, value in row.items():
            if pd.isna(value):
                continue  # Skip if the value is NaN

            value = str(value).lower()  # Convert to lowercase for case-insensitive matching
            tokens = re.split(r'\W+', value)  # Split into words based on non-alphanumeric characters

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
                required=True,
            )
        },
    )


def split_dataframe(edited_df: pd.DataFrame) -> None:
    """
    Split the edited DataFrame based on the 'OHT_Class' column and store the grouped DataFrames in the session state.
    Args:
        edited_df (pd.DataFrame): The edited DataFrame.
    """
    grouped_dfs = {category: df for category, df in edited_df.groupby("OHT_Class")}
    st.session_state.grouped_dfs = grouped_dfs
    st.success(f"Original data split into: {len(grouped_dfs)} dataframes")
    for category, df in grouped_dfs.items():
        st.write(f"DataFrame for OHT_Class '{category}' has {len(df)} rows.")
    st.session_state.split_done = True


def merge_columns(modified_df: pd.DataFrame, merge_col1: str, merge_col2: str, new_merge_col_name: str) -> None:
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
            + " "
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


def map_columns(modified_df: pd.DataFrame, unique_cols: set, uploaded_mappings: dict = None, field_suggestions: dict = None) -> dict:
    columns_to_map = list(modified_df.columns)
    columns_to_map.remove('OHT_Class')
    columns_to_map.remove('Classification_Reasoning')

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

    st.write("**Map your columns:**")
    column_config = {
        "User Column": st.column_config.Column("User Column", width='large'),
        "OHT Column": st.column_config.SelectboxColumn(
            "OHT Column",
            width="large",
            options=list(unique_cols),
            required=False,
        ),
        "Machine Suggested Column Mapping": st.column_config.Column("Machine Suggested Column Mapping", width='large'),
        "Expected Value Type": st.column_config.SelectboxColumn(
            "Expected Value Type",
            width="medium",
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
    )
    st.download_button(
        label="Download Modified Data",
        data=modified_df.to_csv(index=False).encode("utf-8"),
        file_name="modified_data.csv",
        mime="text/csv",
    )


def display_word_document(oht_docx_path: str) -> None:
    """
    Display the Word document for the selected OHT.
    Args:
        oht_docx_path (str): The path to the Word document.
    """
    with (st.expander("Click to show WORD document for the OHT")):
        with open(oht_docx_path, 'rb') as doc:
            result_html = mammoth.convert_to_html(doc)
            html_content = result_html.value
            st.markdown(
                f'<iframe srcdoc="{html_content}" height="600" width="100%" frameborder="0" scrolling="yes"></iframe>',
                unsafe_allow_html=True)
                #html_content, height=600, scrolling=True)


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


def create_platform_metadata(oht_type):
    return {
        "iuclidVersion": "7.0.7",
        "documentKey": f"{generate_uuid()}/{generate_uuid()}",
        "parentDocumentKey": "",
        "name": "",
        "documentType": oht_type,
        "documentSubType": "",
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
    module_name = f"{oht_type.lower()}_6_5.models"
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


def map_csv_to_oht_instances(data, test_material_uuid_map, test_material_columns, substance_uuid_map, substance_columns):
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
        #st.write(oht_instance)

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
            oht_instance.uuid = f"{generate_uuid()}/{generate_uuid()}"

        oht_instances.append((oht_instance, substance_uuid))
    #st.write('done')
    return oht_instances


def create_xml_serializer(oht_type):
    # Initialize the XML context with the package containing the OHT models
    try:
        context = XmlContext(models_package=f"{oht_type.lower()}_6_5.models")
    except Exception as e:
        print("Error in create_xml_serializer:", e)
    # Build the context recursively to include all related classes
    context.build_recursive(get_oht_classes(oht_type)[0])

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


def instance_to_i6d(instance, output_dir, oht_type, parent_key=None, is_attachment=False):
    """Convert an instance to an i6d XML file."""
    # Create an XML serializer and namespace mapping for the given OHT type
    serializer, ns_map = create_xml_serializer(oht_type)

    # Serialize the instance to XML
    xml_content = serializer.render(instance, ns_map)

    # Remove the XML declaration from the serialized content
    xml_content = xml_content.split("?>", 1)[1].strip()
    document_type = to_document_type_format(oht_type)
    # Create platform metadata for the i6d file
    platform_metadata = create_platform_metadata(document_type)
    if parent_key:
        platform_metadata['parentDocumentKey'] = parent_key
    platform_metadata['documentKey'] = instance.uuid

    # Format the platform metadata as an XML string
    platform_metadata_xml = f"""
    <PlatformMetadata xmlns="http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1">
        <iuclidVersion>{platform_metadata['iuclidVersion']}</iuclidVersion>
        <documentKey>{platform_metadata['documentKey']}</documentKey>
        <parentDocumentKey>{platform_metadata['parentDocumentKey']}</parentDocumentKey>
        <name>{platform_metadata['name']}</name>
        <documentType>{platform_metadata['documentType']}</documentType>
        <documentSubType>{platform_metadata['documentSubType']}</documentSubType>
        <orderInSectionNo>{platform_metadata['orderInSectionNo']}</orderInSectionNo>
        <definitionVersion>{platform_metadata['definitionVersion']}</definitionVersion>
        <creationDate>{platform_metadata['creationDate']}</creationDate>
        <lastModificationDate>{platform_metadata['lastModificationDate']}</lastModificationDate>
        <submissionType>{platform_metadata['submissionType']}</submissionType>
        <submissionTypeVersion>{platform_metadata['submissionTypeVersion']}</submissionTypeVersion>
        <submittingLegalEntity>{platform_metadata['submittingLegalEntity']}</submittingLegalEntity>
        <dossierSubject>{platform_metadata['dossierSubject']}</dossierSubject>
        <i5Origin>{platform_metadata['i5Origin']}</i5Origin>
        <creationTool>{platform_metadata['creationTool']}</creationTool>
        <snapshotCreationTool>{platform_metadata['snapshotCreationTool']}</snapshotCreationTool>
    </PlatformMetadata>
    """

    # Define the namespace mapping for the entire i6d document
    ns_map = {
        None: f"http://iuclid6.echa.europa.eu/namespaces/ENDPOINT_STUDY_RECORD-{oht_type}/9.0",  # Default namespace
        "i6c": "http://iuclid6.echa.europa.eu/namespaces/platform-container/v2",  # Namespace for platform container
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",  # XML Schema instance namespace
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
    file_path = os.path.join(output_dir, f"{document_key}.i6d")

    # Write the XML tree to a file
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    return document_key


def create_manifest(i6d_files, file_path):
    """Create a manifest XML file that lists all i6d files."""
    # Create the root element for the manifest
    root = etree.Element("Manifest")

    # Add an entry for each i6d file to the manifest
    for i6d_file in i6d_files:
        entry = etree.SubElement(root, "Entry")  # Create an Entry element
        entry.text = i6d_file  # Set the text of the Entry element to the i6d file name

    # Create an XML tree from the root element
    tree = etree.ElementTree(root)

    # Write the XML tree to a file
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")


def save_dataframe_as_excel(data, file_path):
    data.to_excel(file_path, index=False)


def generate_i6z(endpoint_instances, test_material_instances, legal_entity_instances, ref_sub_instances,
                 substance_instances, output_dir, i6z_file_path, data, other_files):
    """Generate an i6z file containing multiple instances."""
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    i6d_files = []  # List to store the names of i6d files
    if test_material_instances is not None:
        for i, instance in enumerate(test_material_instances):
            # Determine the OHT type from the instance class name
            oht_type = type(instance).__name__.replace("TestMaterialInformation", "")
            document_key = instance_to_i6d(instance, output_dir, "TestMaterialInformation")
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if legal_entity_instances is not None:
        for i, instance in enumerate(legal_entity_instances):
            document_key = instance_to_i6d(instance, output_dir, "LegalEntity")
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if ref_sub_instances is not None:
        for i, instance in enumerate(ref_sub_instances):
            document_key = instance_to_i6d(instance, output_dir, "ReferenceSubstance")
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    if substance_instances is not None:
        for i, instance in enumerate(substance_instances):
            document_key = instance_to_i6d(instance, output_dir, "Substance")
            i6d_file_path = f"{document_key}.i6d"
            i6d_files.append(i6d_file_path)

    for i, (instance, parent_key) in enumerate(endpoint_instances):
        # Determine the OHT type from the instance class name
        oht_type = type(instance).__name__.replace("EndpointStudyRecord", "")
        #st.write(oht_type)
        document_key = instance_to_i6d(instance, output_dir, oht_type, parent_key)
        #st.write(document_key)
        i6d_file_path = f"{document_key}.i6d"
        # Define the file path for the i6d file
        #i6d_file_path = os.path.join(output_dir, f"instance_{i + 1}.i6d")

        # Convert the instance to an i6d file
        #instance_to_i6d(instance, i6d_file_path, oht_type)

        # Add the i6d file name to the list
        i6d_files.append(i6d_file_path)
    #st.write(f"Uploaded Attachments: {other_files}")
    if other_files is not None:
        attach_keys = []
        for attachment in other_files:
            document_key = create_i6d_for_attachment(attachment, output_dir)
            attach_keys.append(f"{document_key}.i6d")

    # Define the file path for the manifest
    manifest_file_path = os.path.join(output_dir, "manifest.xml")

    # Create the manifest file
    create_manifest(i6d_files, manifest_file_path)
    main_data = os.path.join(output_dir, "data.xlsx")
    save_dataframe_as_excel(data, main_data)
    other_file_paths = save_uploaded_files(other_files, output_dir)
    # Create a zip file (i6z file) containing the manifest and i6d files
    with zipfile.ZipFile(i6z_file_path, 'w', zipfile.ZIP_DEFLATED) as i6z:
        i6z.write(manifest_file_path, os.path.basename(manifest_file_path))  # Add the manifest file
        for i6d_file in i6d_files:
            i6z.write(os.path.join(output_dir, i6d_file), i6d_file)  # Add each i6d file
        i6z.write(main_data, os.path.basename(main_data))
        if other_files is not None:
            for i in range(0, len(other_files)):
                file_path = os.path.join(output_dir, other_files[i].name)
                with open(file_path, 'wb') as f:
                    f.write(other_files[i].getvalue())
                i6z.write(file_path, attach_keys[i])
        for file_path in other_file_paths:
            i6z.write(file_path, os.path.basename(file_path))


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


def create_test_material_instances(data, test_material_columns):
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
        uuid_str = f"{generate_uuid()}/{generate_uuid()}"
        test_material_instance.uuid = uuid_str
        test_material_instances.append(test_material_instance)
        test_material_values = tuple(row[col] for col in test_material_columns)
        test_material_uuid_map[test_material_values] = uuid_str

    return test_material_instances, test_material_uuid_map


def create_substance_instances(data, substance_columns, ref_sub_uuid_map, ref_sub_columns):
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
        uuid_str = f"{generate_uuid()}/{generate_uuid()}"
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


def create_legal_entity_instances(data, legal_entity_columns):
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
        uuid_str = f"{generate_uuid()}/{generate_uuid()}"
        legal_entity_instance.uuid = uuid_str
        legal_entity_instances.append(legal_entity_instance)
        legal_entity_values = tuple(row[col] for col in legal_entity_columns)
        legal_entity_uuid_map[legal_entity_values] = uuid_str

    return legal_entity_instances, legal_entity_uuid_map


def create_ref_sub_instances(data, ref_sub_columns):
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
        uuid_str = f"{generate_uuid()}/{generate_uuid()}"
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
        #print('actual_type:')
        #print(type(actual_type))
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
        module_name = f"{model_name.lower()}_6_5.models"
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
    file_extension = file_name.split(".")[-1].lower()
    if file_extension == "pdf":
        return "application/pdf"
    elif file_extension == "png":
        return "image/png"
    elif file_extension == "jpg" or file_extension == "jpeg":
        return "image/jpeg"
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")


def create_i6d_for_attachment(attachment_file, output_dir):
    file_name = attachment_file.name
    file_content = attachment_file.getvalue()
    md5_hash = compute_mp5(file_content)
    mime_type = determine_mime_type(file_name)
    document_key = f"{generate_uuid()}/{generate_uuid()}"
    creation_date = datetime.datetime.utcnow().isoformat() + "Z"
    root = etree.Element("Attachment",
                         nsmap={
                             None: "http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1",
                             "xlink": "http://www.w3.org/1999/xlink",
                             "xsi": "http://www.w3.org/2001/XMLSchema-instance"
                         }
    )

    etree.SubElement(root, 'documentKey').text = document_key
    etree.SubElement(root, "name").text = file_name
    etree.SubElement(root, "creationDate").text = creation_date
    etree.SubElement(root, "lastModificationDate").text = creation_date
    etree.SubElement(root, "md5").text = md5_hash
    etree.SubElement(root, "mimetype").text = mime_type

    content = etree.SubElement(root, "content", {
        "{http://www.w3.org/1999/xlink}href": f"attachments/{md5_hash}.{file_name.split('.')[-1]}",
        "{http://www.w3.org/1999/xlink}type": "simple"
    })
    # etree.SubElement(root, "content",
    #                  attrib={"{http://www.w3.org/1999/xlink}href": f"attachments/{md5_hash}.{file_name.split('.')[-1]}",
    #                          "{http://www.w3.org/1999/xlink}type": "simple"})

    # attachment_content = f"""
    # <Attachment xmlns="http://iuclid6.echa.europa.eu/namespaces/platform-attachment/v1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    #     <documentKey>{document_key}</documentKey>
    #     <name>{file_name}</name>
    #     <creationDate>{creation_date}</creationDate>
    #     <lastModificationDate>{creation_date}</lastModificationDate>
    #     <md5>{md5_hash}</md5>
    #     <mimetype>{mime_type}</mimetype>
    #     <content xlink:href="attachments/{md5_hash}.{file_name.split('.')[-1]}" xlink:type="simple"/>
    # </Attachment>
    # """
    document_key_clean = document_key.replace("/", "_")
    file_path = os.path.join(output_dir, f"{document_key_clean}.i6d")
    #root = etree.fromstring(attachment_content)
    #root = root.split("?>", 1)[1].strip()

    tree = etree.ElementTree(root)
    tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="UTF-8")
    return document_key_clean
