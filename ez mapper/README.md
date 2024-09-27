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

Clone the repository and install the required dependencies:
 - pandas
 - streamlit
 - openpyxl

### Usage

To start the EZ Mapper, run the following command in your terminal:

```streamlit run ezmapper.py```

The web application will be hosted locally and you can access it through your web browser at the address provided by Streamlit.

Project Structure

 - ezmapper.py: The main Python script that runs the Streamlit web application.
 - utils.py: Functions that are imported by ezmapper.py
 - All OHTs Word Files -Nov 2021: Directory containing Word files for OHT templates.
 - All ______6_5 folders: Formatting files for each OHT to assist with i6z generation and field options
