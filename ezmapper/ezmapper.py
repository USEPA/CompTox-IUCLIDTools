import warnings
from pathlib import Path
import json
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx
import pandas as pd
import importlib
import zipfile
from io import BytesIO
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from ez_utils import *
import logging
import main as suggestion_logic
from configs.config import config
import threading
import time
import logging

st.set_page_config(layout="wide")
#temp_field_suggestions = None
suggestions_lock = threading.Lock()
# Suppress specific warnings from openpyxl that are not relevant for the user
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

# Set the title and description of the web app
st.title("EZ Mapper")
st.markdown("A tool for mapping and transforming data to an i6z file.")

# Define the directory path for OHT files
directory_path = Path("All OHTs Word Files -Nov 2021")
# Define the directory path for OHT excel files
oht_excel_base_path = Path("oht_excel_files")

# Load OHT files
oht_files = load_oht_files(directory_path)

# Initialize session state variables to manage user session data
initialize_session_state()

if "field_suggestions" not in st.session_state:
    st.session_state['field_suggestions'] = {}
if "suggestions_done" not in st.session_state:
    st.session_state['suggestions_done'] = False

# Create a sidebar for user inputs
st.sidebar.title("Upload File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
st.sidebar.title("Upload Column Mapping")
uploaded_json = st.sidebar.file_uploader("Upload a previously saved column mapping JSON", type=['json'])
st.sidebar.title("Upload Other Files")
uploaded_other_files = st.sidebar.file_uploader("Choose files to upload", accept_multiple_files=True)

suggestions_status_placeholder = st.empty()


def background_suggestions_logic(user_df, results):
    global temp_field_suggestions
    try:
        placeholder_test = suggestion_logic.main(config, user_df)
        temp_field_suggestions = placeholder_test
        print(temp_field_suggestions)
        st.session_state['suggestions_done'] = True
        st.session_state['field_suggestions'] = temp_field_suggestions
        results[0] = temp_field_suggestions
        print(st.session_state['field_suggestions'])
    #st.session_state['suggestions_running'] = False
        print('suggestions done')
        #st.rerun()
    except Exception as e:
        st.error(f"Error running suggestions logic: {e}")


# Process the uploaded file if it exists
if uploaded_file is not None:
    user_df = upload_file_to_df(uploaded_file)
    st.session_state.user_df = user_df

    base_file_name = Path(uploaded_file.name).stem

    # Display a preview of the data
    display_data_preview(user_df)

    # Classify data based on predefined criteria
    user_df = classify_data(user_df)

    if not st.session_state["suggestions_done"]:
        with st.spinner("Running machine suggestions in the background..."):
            if "suggestions_thread" not in st.session_state:
                results = [None]
                suggestions_thread = threading.Thread(target=background_suggestions_logic, args=(user_df, results))
                add_script_run_ctx(suggestions_thread)
                suggestions_thread.start()
                #suggestions_thread.join()
                #st.session_state['suggestions_running'] = True
                st.session_state['suggestions_thread'] = suggestions_thread
                #st.rerun()
        #st.session_state['field_suggestions'] = suggestion_logic.main(config, user_df)
    #field_suggestions = suggestion_logic.main(config, user_df)

    # Classify button
    st.markdown(
        "Classify Rows and Split Data by OHT Classification"
    )
    classify_button = st.button("Classify Data")

    # Handle classify button press
    if classify_button:
        st.write("**Verify and Edit Classifications:**")
        st.session_state.classify_pressed = True
        st.session_state["edited_df"] = user_df.copy()
else:
    # Clear session state and stop execution if 'x' is clicked in the sidebar by the file
    st.session_state.clear()
    st.stop()

# Display the data editor once the classify button has been pressed
if "edited_df" in st.session_state and st.session_state.classify_pressed:
    edited_df = st.session_state["edited_df"]
    display_data_editor(edited_df, oht_files)

    # Confirm button to finalize the data split based on classification
    confirm_button = st.button("Confirm")
    if confirm_button:
        edited_df = st.session_state.df1
        split_dataframe(edited_df)

# Dropdown menu for selecting a DataFrame to map columns after splitting
if st.session_state.get("split_done", False):
    selected_df_key = st.sidebar.selectbox(
        "Select a DataFrame to Map Columns:",
        options=["None"] + list(st.session_state.grouped_dfs.keys()),
        index=0,
        key="selected_df_key",
    )

    # Display the selected DataFrame if a valid selection is made
    if selected_df_key != "None":
        st.session_state.selected_df = st.session_state.grouped_dfs[selected_df_key]
        st.write(
            f"DataFrame for {selected_df_key} has {len(st.session_state.selected_df)} rows."
        )

        # Initialize session state for the DataFrame if it doesn't exist
        if "modified_df" not in st.session_state:
            st.session_state.modified_df = st.session_state.selected_df.copy()

# Section for merging or splitting columns in the DataFrame
if st.session_state.split_done and selected_df_key != "None":
    selected_oht = selected_df_key
    st.session_state.selected_oht = selected_oht
    oht_docx_path = oht_files[selected_oht]["docx"]
    st.session_state.oht_docx_path = oht_docx_path

    st.write("**Merge Columns**")
    col1, col2, new_col_name = st.columns(3)
    with col1:
        merge_col1 = st.selectbox(
            "First column to merge:",
            [""] + list(st.session_state.modified_df.columns),
            key="merge_col1",
        )
    with col2:
        merge_col2 = st.selectbox(
            "Second column to merge:",
            [""] + list(st.session_state.modified_df.columns),
            key="merge_col2",
        )
    with new_col_name:
        new_merge_col_name = st.text_input(
            "Enter the new column name:", key="new_merge_col_name"
        )

    # Merge columns based on user selection
    if st.button("Merge Columns"):
        merge_columns(st.session_state.modified_df, merge_col1, merge_col2, new_merge_col_name)

    # Section for splitting columns based on a delimiter
    st.write("**Split Column**")
    split_col, delimiter, maxsplit = st.columns(3)
    with split_col:
        column_to_split = st.selectbox(
            "Select the column to split:",
            [""] + list(st.session_state.modified_df.columns),
            key="split_col",
        )
    with delimiter:
        split_delimiter = st.text_input("Enter the delimiter:", key="split_delimiter")
    with maxsplit:
        split_maxsplit = st.number_input(
            "Max number of splits:", min_value=1, value=1, key="split_maxsplit"
        )

    # Split the column based on user inputs
    if st.button("Split Column"):
        split_column(st.session_state.modified_df, column_to_split, split_delimiter, split_maxsplit)

    uploaded_mappings = {}

    if uploaded_json is not None:
        try:
            uploaded_mappings = json.load(uploaded_json)
            st.sidebar.success("Column mapping JSON uploaded successfully")
        except json.JSONDecodeError:
            st.sidebar.error("Invalid JSON file. Please upload a valid column mapping JSON file.")

    # Check if the user has made a selection
    if selected_oht:
        # Extract the OHT number from the selected key
        oht_parts = selected_oht.split(":")
        oht_number = oht_parts[0].strip()
        oht_type = oht_parts[1].strip().replace(" ", "") if len(oht_parts) > 1 else oht_number

        # Construct the path to the specific OHT directory
        oht_excel_dir_path = oht_excel_base_path / oht_number
        # Check if the OHT directory exists

        model_names = ["LegalEntity", "ReferenceSubstance", "Substance", "TestMaterialInformation"]
        unique_cols = load_and_introspect_models(model_names)

        oht_class, _ = get_oht_classes(oht_type)
        endpoint_fields = get_model_fields(oht_class, f"ENDPOINT_STUDY_RECORD.{oht_type}")
        unique_cols.update(endpoint_fields)

        #column_mapping = map_columns(st.session_state.modified_df, unique_cols, uploaded_mappings, st.session_state['field_suggestions'])
        #suggestions_status_placeholder.info(f"Checking suggestions: {st.session_state.get('suggestions_done')}")
        if "suggestions_thread" in st.session_state:
            if not st.session_state['suggestions_thread'].is_alive():
                #st.session_state['field_suggestions'] = temp_field_suggestions
                print('field suggestions')
                print(st.session_state['field_suggestions'])
                #print('results')
                #print(results[0])
                suggestions_status_placeholder.info("Machine suggestions finished!")
                column_mapping = map_columns(st.session_state.modified_df, unique_cols, uploaded_mappings,
                                         st.session_state['field_suggestions'])
            else:
                suggestions_status_placeholder.info("Machine suggestions are still running...")
                column_mapping = map_columns(st.session_state.modified_df, unique_cols, uploaded_mappings, {})
            # while not st.session_state.get('suggestions_done', False):
            #     time.sleep(1)
            #     st.rerun()
        # if st.session_state.get('suggestions_done', ):
        #     suggestions_status_placeholder.info("Machine suggestions finished!")
        #     column_mapping = map_columns(st.session_state.modified_df, unique_cols, uploaded_mappings,
        #                                  st.session_state['field_suggestions'])

        # Preview the column mapping before finalizing
        if st.button("Preview Column Mapping"):
            data = apply_column_mapping(column_mapping, st.session_state.modified_df)
            preview_column_mapping(column_mapping, data)

            # # Add button for i6z file generation
        generate_i6z_button = st.button("Generate i6z File")
        if generate_i6z_button:
            #st.write('generating')
            try:
                column_mapping_dict = column_mapping
                data = apply_column_mapping(column_mapping, st.session_state.modified_df)
                test_material_columns = get_test_material_columns(column_mapping_dict)
                #tm_data = data[[col for col in data.columns if col in test_material_columns]]
                if test_material_columns:
                    test_material_instances, test_material_uuid_map = create_test_material_instances(data,
                                                                                                 test_material_columns)
                else:
                    test_material_instances, test_material_uuid_map = None, None
                #data = data.drop(columns=[col for col in test_material_columns if col in data.columns])
                legal_entity_columns = get_legal_entity_columns(column_mapping_dict)
                #le_data = data[[col for col in data.columns if col in legal_entity_columns]]
                if legal_entity_columns:
                    legal_entity_instances, legal_entity_uuid_map = create_legal_entity_instances(data,
                                                                                              legal_entity_columns)
                else:
                    legal_entity_instances, legal_entity_uuid_map = None, None
                #data = data.drop(columns=[col for col in legal_entity_columns if col in data.columns])

                ref_sub_columns = get_ref_sub_columns(column_mapping_dict)

                #ref_data = data[[col for col in data.columns if col in ref_sub_columns]]
                if ref_sub_columns:
                    ref_sub_instances, ref_sub_uuid_map = create_ref_sub_instances(data, ref_sub_columns)
                else:
                    ref_sub_instances, ref_sub_uuid_map = None, None
                #data = data.drop(columns=[col for col in ref_sub_columns if col in data.columns])

                substance_columns = get_substance_columns(column_mapping_dict)
                #sub_data = data[[col for col in data.columns if col in substance_columns]]
                if substance_columns:
                    substance_instances, substance_uuid_map = create_substance_instances(data, substance_columns, ref_sub_uuid_map, ref_sub_columns)
                else:
                    substance_instances, substance_uuid_map = None, None
                #data = data.drop(columns=[col for col in substance_columns if col in data.columns])
                #st.write('prestuff')

                oht_instances = map_csv_to_oht_instances(data, test_material_uuid_map, test_material_columns,
                                                         substance_uuid_map, substance_columns)
                output_dir = 'output'
                i6z_file_path = 'output/data.i6z'
                generate_i6z(oht_instances, test_material_instances, legal_entity_instances, ref_sub_instances,
                             substance_instances, output_dir, i6z_file_path, data, uploaded_other_files)

                st.write("Successfully Generated")
                outfile_name = base_file_name + '.i6z'
                st.download_button(
                    label='Download i6z File',
                    data=open(i6z_file_path, 'rb').read(),
                    file_name=outfile_name,
                    mime='application/octet-stream'
                )
            except Exception as e:
                st.error(f"Error generating: {e}")

        # Display the associated Word document for the OHT
        display_word_document(oht_docx_path)
