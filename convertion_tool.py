import streamlit as st
import pandas as pd
import os
import zipfile
from io import BytesIO
from lxml import etree
from ez_utils import (
    extract_i6z_files,
    process_single_i6d,
    create_new_i6z,
    get_entity_type,
    normalize_path,
)


def get_definition_version(version):
    for step in version_steps:
        if step["version"] == version:
            return step["definition_version"]
    return "8.0"  # fallback

# Supported versions and their definitionVersion values
version_steps = [
    {"version": "6.8", "definition_version": "8.0"},
    {"version": "6.7", "definition_version": "7.0"},
    {"version": "6.6", "definition_version": "6.0"},
    # Add more as needed
]

# Map each step to its folder
conversion_folders = {
    ("6.8", "6.7"): "6.8_6.7_changes",
    ("6.7", "6.6"): "6.7_6.6_changes",
    ("6.6", "6.5"): "6.6_6.5_changes",
    # Add more as needed
}

st.title("IUCLID i6z File Converter")
st.write("Convert your IUCLID `.i6z` files to a new version of IUCLID.")

uploaded_file = st.file_uploader("Upload an i6z file", type=["i6z"])

i6d_files = []
definition_versions = set()

if uploaded_file:
    with st.spinner("Extracting i6z file..."):
        extract_dir = "extracted_i6d_files"
        os.makedirs(extract_dir, exist_ok=True)
        i6d_files = extract_i6z_files(uploaded_file, extract_dir)
        st.success(f"Extracted {len(i6d_files)} .i6d files from the uploaded i6z file.")

    # Step 1.5: Check definitionVersion in all i6d files
    for i6d_file in i6d_files:
        try:
            tree = etree.parse(i6d_file)
            root = tree.getroot()
            ns = {
                "i6c": "http://iuclid6.echa.europa.eu/namespaces/platform-container/v2",
                "i6m": "http://iuclid6.echa.europa.eu/namespaces/platform-metadata/v1"
            }
            def_ver_elem = root.find(".//i6c:PlatformMetadata/i6m:definitionVersion", namespaces=ns)
            if def_ver_elem is not None and def_ver_elem.text:
                definition_versions.add(def_ver_elem.text.strip())
        except Exception as e:
            st.warning(f"Error reading definitionVersion from {i6d_file}: {e}")

    # Display the definitionVersion info
    if len(definition_versions) == 1:
        st.info(f"All i6d files have definitionVersion: {list(definition_versions)[0]}")
    elif len(definition_versions) > 1:
        st.warning(f"Different definitionVersions found in i6d files: {', '.join(definition_versions)}")
    else:
        st.warning("No definitionVersion found in any i6d file.")

    # User selects target version
    target_version = st.selectbox("Select IUCLID Version to Convert to", ["6.7", "6.6"], index=0)
    TARGET_VERSION = target_version.replace(".", "_")
    ENTITY_MODELS_FOLDER = f"entity_models_{TARGET_VERSION}"

    # Determine input version from definition_versions
    input_def_ver = list(definition_versions)[0] if len(definition_versions) == 1 else None
    input_version = None
    for step in version_steps:
        if step["definition_version"] == input_def_ver:
            input_version = step["version"]
            break

    if not input_version:
        st.error("Could not determine input IUCLID version from definitionVersion.")
        st.stop()

    # Determine conversion path
    def get_conversion_path(input_version, target_version, version_steps):
        idx_input = next(i for i, v in enumerate(version_steps) if v["version"] == input_version)
        idx_target = next(i for i, v in enumerate(version_steps) if v["version"] == target_version)
        if idx_input > idx_target:
            # Need to step down through each version
            return [(version_steps[i]["version"], version_steps[i+1]["version"])
                    for i in range(idx_input, idx_target, -1)]
        else:
            return []

    conversion_path = get_conversion_path(input_version, target_version, version_steps)

    if st.button("Convert i6z File"):
        try:
            current_i6d_files = i6d_files
            for from_ver, to_ver in conversion_path:
                folder = conversion_folders.get((from_ver, to_ver))
                definition_version = get_definition_version(to_ver)
                if not folder:
                    st.error(f"No conversion folder for {from_ver} to {to_ver}")
                    st.stop()
                with st.spinner(f"Applying conversion: {from_ver} → {to_ver}"):
                    definitions_files = [
                        os.path.join(folder, f)
                        for f in os.listdir(folder)
                        if f.endswith(".xlsx")
                    ]
                    definitions_dfs = []
                    for file_path in definitions_files:
                        try:
                            df = pd.read_excel(file_path, sheet_name="Definitions")
                            df["To Value"] = df["To Value"].apply(normalize_path)
                            df["From Value"] = df["From Value"].apply(normalize_path)
                            definitions_dfs.append(df)
                        except Exception as e:
                            st.warning(f"Error loading definitions file {file_path}: {e}")
                    if not definitions_dfs:
                        st.error(f"No valid definitions files found in {folder}.")
                        st.stop()
                    definitions_df = pd.concat(definitions_dfs, ignore_index=True)
                    # Process each i6d file for this step
                    output_dir = f"output_{from_ver}_to_{to_ver}"
                    os.makedirs(output_dir, exist_ok=True)
                    next_i6d_files = []
                    for i6d_file in current_i6d_files:
                        st.write(f"Processing file: {i6d_file}")
                        try:
                            tree = etree.parse(i6d_file)
                            root = tree.getroot()
                            entity_type = get_entity_type(root)
                            if entity_type.lower() == "dossier":
                                st.info(f"Skipping dossier entity for file: {i6d_file}")
                                continue
                            output_file = process_single_i6d(i6d_file, definitions_df, to_ver, output_dir, definitions_df=definitions_df)
                            next_i6d_files.append(output_file)
                        except Exception as e:
                            st.warning(f"Error processing file {i6d_file}: {e}")
                    current_i6d_files = next_i6d_files

            # After all steps, create new i6z and provide download as before
            with st.spinner("Creating new i6z file..."):
                final_output_dir = output_dir if conversion_path else extract_dir
                new_i6z_path = os.path.join(final_output_dir, "updated_dossier.i6z")
                create_new_i6z(final_output_dir, new_i6z_path, uploaded_file)
                st.success("New i6z file created successfully.")

            with open(new_i6z_path, "rb") as f:
                st.download_button(
                    label="Download Converted i6z File",
                    data=f,
                    file_name="converted_i6z_file.i6z",
                    mime="application/zip",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")