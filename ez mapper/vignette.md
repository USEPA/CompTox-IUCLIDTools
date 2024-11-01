# EZ Mapper Vignette

## 1. Introduction and Purpose
**Description**: EZ Mapper is a tool designed for data transformation and mapping to the i6z format. This vignette provides an overview of the app’s key functionality and a step-by-step example of how to use the provided test input file.  
**Objective**: Guide users on how to upload data, classify rows, map columns, and generate an i6z file.

---

## 2. Setup and Installation
1. **Ensure dependencies are installed** by running:
   ```bash
   pip install -r requirements.txt
2. **Launch EZMapper** by running:
   ```bash
   streamlit run ezmapper.py
3. The app will open in your default broswer, where you can follow the steps below.
![Default](default_app.png)
---

## 3. Test Case Walkthrough
Using the test input "oht67test.csv" file with EZMapper, let's go thorugh a complete example.
### Step 1: Uploading Your Files
- In the sidebar, go to Upload File and Select the test input file (oht67test.csv).
- You may also click on Upload Column Manpping and select the json file (column_mapping.json).
![leftpanel](left_panel.png)
### Step 2: Classifying Data
1. After uploading your file, a preview will display in the main panel to the right.
2. The machine suggestions logic will begin running in the background for column mappings.
3. Click on Classify Data to initiate data classification.
4. A new table will appear. The first column will give the recommended OHT for that row and the second column the reasoning for that recommendation.
### Step 3: Verifying and Editing Classifications
1. You can click on the values in the first column to manually set the OHT for each row.
2. Click Confirm when you are done.
![ohtclass](oht_identify.png)
### Step 4: Choose DataFrame
1. At the bottom of the left panel, a new option to select a DataFrame appears.
2. Select from the dropdown which DataFrame you want to work with and several more sections will appear in the main panel.
### Step 5: Modifying Data
- Merge Columns: Combine data from two columns into a new one.
- Split Columns: Split a column into multiple columns based on a delimiter.
![splitmerge](split_merge.png)
### Step 6: Map Your Columns
1. At the bottom of the panel, there is an option to "Click to show WORD document for the OHT" that shows the OECD Harmonised Template document for the chosen OHT. This file can help guide mapping decisions.
2. There will be a table with "User Column" with all columns in the user submitted data.
3. The second "OHT Column" allows you to click each cell and assign a OHT field mapping. You can start typing to reduce dropdown options. This column will also be prepopulated with any existing mappings based on you uploaded column mapping JSON file.
3. The third "Machine Suggestion Column Mapping" column will be populated with any and all suggested mappings based on the machine learning logic. This may not be populated at first but will update when the logic is finished running. There is a progress message at the top of the panel.
### Step 7: Exporting Files
- Preview Column Mapping: Clicking this button will display a preview of the column mapping JSON file based on the mappings in the table above.
- Download Column Mapping: This button will download the JSON file to your browser.
- Generate i6z File: Once you are happy with the mappings, clicking this button generates the i6z file with each individual i6d file being structurally accurate based on the xml format files from IUCLID.
- Download i6z File: Once the i6z file has been generated, you can then download the i6z file into your local browser.
