# EZ Mapper

EZ Mapper is a web application built with Streamlit that allows users to easily map and manipulate data columns. It provides functionalities to merge and split columns, preview data, and download modified data and column mappings. It also allows for the creation and download of structurally accurate i6z files for the modified data.

### Features

- File upload for CSV and Excel files
- Data preview
- Column merging and splitting
- Column mapping for specific templates (OHT files)
- Downloadable modified data and column mapping JSON
- Upload column mapping JSON for automatic mapping on new data
- Generate and download i6z files of IUCLID formatted data

### Installation
- Ensure you are using python 3.8.
- Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
### Usage

To start the EZ Mapper, run the following command in your terminal:

```streamlit run ezmapper.py```

The web application will be hosted locally and you can access it through your web browser at the address provided by Streamlit.

Project Structure

 - ezmapper.py: The main Python script that runs the Streamlit web application.
 - ez_utils.py: Functions that are imported by ezmapper.py
 - main.py: The main file that starts the machine suggestion logic.
 - src: This folder contains the supporting files for the machine suggestion logic.
 - configs: Contains a config file for the machine suggestion logic.
 - data and output: Supporting folders for the machine suggestions input and output.
 - test_files: Contains some example test files and also a vignette which has a walkthrough for the test data.
 - All OHTs Word Files -Nov 2021: Directory containing Word files for OHT templates.
 - entity_models: Contains formatting files for each OHT to assist with i6z generation and field options. These are broken into each individual entity.
