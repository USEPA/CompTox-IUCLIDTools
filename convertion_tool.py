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


DEFINITIONS_FOLDER = "changes_files"
DEFINITIONS_FILES_BY_STEP = {
    ("6_8", "6_7"): [
        "Full_Comparison_OECD_v8.15-v9.13_fake_testing.xlsx",
        "Full_Comparison_CORE_v8.14-v9.16.xlsx",
        "Full_Comparison_DOMAIN_v5.10-v6.9.xlsx",
        "Full_Comparison_AU_IND_CHEM_v5.3-v6.3.xlsx",
        "Full_Comparison_EU_BPR_v8.9-v9.8.xlsx",
        "Full_Comparison_EU_CLP_v8.3-v9.6.xlsx",
        "Full_Comparison_EU_DWD_v1.9-v2.11.xlsx",
        "Full_Comparison_EU_ECHA_v1.3-v2.3.xlsx",
        "Full_Comparison_EU_EFSA_v1.2-v2.6.xlsx",
        "Full_Comparison_EU_PPP_v4.11-v5.8.xlsx",
        "Full_Comparison_EU_SCIP_v4.0-v5.2.xlsx",
        "Full_Comparison_OECD_v8.15-v9.13.xlsx"
    ],
    ("6_7", "6_6"): [
        "Comparison_AU_IND_CHEM_v5.3-v4.4.xlsx",
        "Comparison_CORE_v8.14-v7.11.xlsx",
        "Comparison_DOMAIN_v5.9-v4.7.xlsx",
        "Comparison_EU_BPR_v8.7-v7.10.xlsx",
        "Comparison_EU_CLP_v8.2-v7.8.xlsx",
        "Comparison_EU_PPP_v4.10-v3.12.xlsx",
        "Comparison_EU_REACH_v8.6-v7.3.xlsx",
        "Comparison_NZ_HSNO_v4.4-v3.0.xlsx",
        "Comparison_OECD_v8.15-v7.8.xlsx"
    ],
    ("6_6", "6_5"): [
        "Comparison_AU_IND_CHEM_v4.4-v3.9.xlsx",
        "Comparison_CORE_v7.11-v6.21.xlsx",
        "Comparison_DOMAIN_v4.7-v3.17.xlsx",
        "Comparison_EU_BPR_v7.10-v6.13.xlsx",
        "Comparison_EU_CLP_v7.7-v6.16.xlsx",
        "Comparison_EU_PPP_v3.10-v2.13.xlsx",
        "Comparison_EU_REACH_v7.3-v6.10.xlsx",
        "Comparison_NZ_HSNO_v3.0-v2.9.xlsx",
        "Comparison_OECD_v7.7-v6.16.xlsx"
    ],
    ("6_5", "6_4"): [
        "Full_Comparison_Application_Tag_IUCLID6_4_6-IUCLID6_5_1_1.xlsx"
    ]
}

def get_mapping_steps(source_version, target_version):
    versions = ["6_8", "6_7", "6_6", "6_5", "6_4"]
    source_version = source_version.strip()
    target_version = target_version.strip()
    debug_msg = (
        f"get_mapping_steps called with:\n"
        f"  source_version: '{source_version}'\n"
        f"  target_version: '{target_version}'\n"
        f"  versions: {versions}\n"
    )
    try:
        source_idx = versions.index(source_version)
    except ValueError:
        raise ValueError(debug_msg + f"  ERROR: source_version '{source_version}' not in versions list!")
    try:
        target_idx = versions.index(target_version)
    except ValueError:
        raise ValueError(debug_msg + f"  ERROR: target_version '{target_version}' not in versions list!")
    debug_msg += f"  source_idx: {source_idx}, target_idx: {target_idx}\n"
    if source_idx < target_idx:
        steps = []
        for i in range(source_idx, target_idx):
            steps.append((versions[i], versions[i + 1]))
        debug_msg += f"  Returning steps: {steps}\n"
        print(debug_msg)
        return steps
    else:
        debug_msg += "  ERROR: Only downgrades are supported (source_idx <= target_idx)\n"
        raise ValueError(debug_msg)

# Streamlit App
st.title("IUCLID i6z File Converter")
st.write("Convert your IUCLID `.i6z` files to a new version of IUCLID. Currently, only version 6.7 is supported.")

# File Upload
uploaded_file = st.file_uploader("Upload an i6z file", type=["i6z"])

i6d_files = []
definition_versions = set()


if uploaded_file:
    # Step 1: Extract the uploaded i6z file
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

    # Now show the version select and conversion button
    version = st.selectbox(
        "Select IUCLID Version to Convert to",
        ["6.8", "6.7", "6.6", "6.5", "6.4"],
        index=0
    )
    target_version = version.replace(".", "_")

    if st.button("Convert i6z File"):
        try:
            # Step 1: Determine source version from definitionVersion
            target_version = version.replace(".", "_")  # e.g., "6.7" → "6_7"
            if len(definition_versions) == 1:
                detected_def_ver = list(definition_versions)[0]
                major_ver = detected_def_ver.split(".")[0]  # e.g., "8"
                source_version = f"6_{major_ver}"           # e.g., "6_8"
                st.info(f"Detected source version: {source_version}")
            else:
                # fallback or error handling
                source_version = "6_8"  # or prompt user

            print(source_version)
            definition_versions = set()
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


            # Step 2: Load definitions for path mappings
            with st.spinner("Loading path mappings..."):
                #source_version = "6_8"  # You can auto-detect later if needed
                mapping_steps = get_mapping_steps(source_version, target_version)
                all_definitions_files = []
                for idx, step in enumerate(mapping_steps):
                    st.info(f"Loading mapping files for step {idx + 1}: {step[0]} → {step[1]}")
                    files = DEFINITIONS_FILES_BY_STEP[step]
                    all_definitions_files.extend(files)
                    st.success(f"Loaded {len(files)} mapping files for {step[0]} → {step[1]}")

                definitions_dfs = []
                for file_name in all_definitions_files:
                    file_path = os.path.join(DEFINITIONS_FOLDER, file_name)
                    try:
                        st.write(f"Loading definitions file: {file_path}")
                        df = pd.read_excel(file_path, sheet_name="Definitions")
                        df["To Value"] = df["To Value"].apply(normalize_path)
                        df["From Value"] = df["From Value"].apply(normalize_path)
                        definitions_dfs.append(df)
                        st.success(f"Loaded: {file_path}")
                    except Exception as e:
                        st.warning(f"Error loading definitions file {file_path}: {e}")
                if definitions_dfs:
                    definitions_df = pd.concat(definitions_dfs, ignore_index=True)
                    st.success("Loaded path mappings successfully.")
                else:
                    st.error("No valid definitions files found.")
                    st.stop()

            # Step 3: Process each i6d file
            with st.spinner("Processing i6d files..."):
                output_dir = "output_directory"
                os.makedirs(output_dir, exist_ok=True)
                for i6d_file in i6d_files:
                    try:
                        tree = etree.parse(i6d_file)
                        root = tree.getroot()
                        entity_type = get_entity_type(root)
                        if entity_type.lower() == "dossier":
                            st.info(f"Skipping dossier entity for file: {i6d_file}")
                            continue
                        process_single_i6d(i6d_file, definitions_df, target_version, output_dir)
                    except Exception as e:
                        st.warning(f"Error processing file {i6d_file}: {e}")
                st.success("All i6d files processed successfully.")

            # Step 4: Create a new i6z file
            with st.spinner("Creating new i6z file..."):
                new_i6z_path = os.path.join(output_dir, "updated_dossier.i6z")
                create_new_i6z(output_dir, new_i6z_path, uploaded_file)
                st.success("New i6z file created successfully.")

            # Step 5: Provide download button
            with open(new_i6z_path, "rb") as f:
                st.download_button(
                    label="Download Converted i6z File",
                    data=f,
                    file_name="converted_i6z_file.i6z",
                    mime="application/zip",
                )
        except Exception as e:
            st.error(f"An error occurred: {e}")