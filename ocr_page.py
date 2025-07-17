import streamlit as st
import subprocess
import os
import io
import tempfile
import zipfile
from configs.config import config

##################################################################################
# Helper Functions
##################################################################################
@st.cache_data(show_spinner = "Running OCR...")
def run_ocr(uploaded_files: io.BytesIO):
    
    with tempfile.TemporaryDirectory() as temp_dir:
        print("Prepping input environment")
        in_doc_dir = os.path.join(temp_dir, 'ocr_docs')
        ocr_text_path = os.path.join(temp_dir, 'ocr_text')
        embedpath = os.path.join(temp_dir, 'ocr_embedded')
        # Create output subfolders
        os.makedirs(in_doc_dir, exist_ok=True)
        os.makedirs(ocr_text_path, exist_ok=True)
        os.makedirs(embedpath, exist_ok=True)

        # Write uploaded files to in_doc_dir
        for f in uploaded_files:
            # Create file paths for OCR process
            file_path = os.path.join(in_doc_dir, f.name)
            # Write input PDF to file
            with open(file_path, "wb") as ff:
                ff.write(f.getbuffer())

        # Prep subprocess command
        # subprocess.run([f"{sys.executable}", "script.py"])
        ocr_cmd = [
            # Path to OCR virtual environment python.exe to use
            config["ocr_venv"],
            "doc_ocr.py",
            '--in_doc_dir',
            in_doc_dir,
            '--ocr_text_path',
            ocr_text_path,
            '--embedpath',
            embedpath,
            '--embed_ocr'
        ]

        # Display terminal output
        # Run the OCR script
        # https://discuss.streamlit.io/t/redirecting-terminal-output/56763
        print("Try running OCR")
        try:
            result = subprocess.Popen(ocr_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = result.communicate()
            print(stdout)
            print(stderr)
            # Display the terminal output
            st.title("Display console output:")
            st.write('\n'.join(stdout.decode().split('\n')[1:][:-1]))

            # Create cached file
            print("Caching output...")
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file: 
                # Iterate through the folder and add its contents to the zip file
                for root, _, files in os.walk(temp_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        # Get the relative path within the archive to avoid including the full source path
                        arcname = os.path.relpath(file_path, temp_dir)
                        print(arcname)
                        # Read selected file
                        with open(file_path, "rb") as f:
                            file_content = f.read()
                        # Write to zip
                        zip_file.writestr(arcname, file_content)

            return zip_buffer
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            st.write(f"An unexpected error occurred: {e}")
    
    return None

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

# Set the title and description of the web app
st.title("EZ Mapper OCR")
st.markdown("A tool for running OCF on PDF files to generate text files and embedded PDFs.")

# Create a sidebar for user inputs
st.sidebar.title("Upload File")
uploaded_files = st.sidebar.file_uploader("Choose a PDF file", 
                                         type=["pdf"], 
                                         accept_multiple_files=True)

# Check if files uploaded
if len(uploaded_files) > 0:
    # Button to run OCR
    if st.button("Run OCR", icon=":material/manufacturing:"):
        ocr_zip = run_ocr(uploaded_files)

        if ocr_zip is not None:
            # Download OCR files
            st.download_button(
                label='Download OCR files',
                icon=":material/download:",
                data=ocr_zip.getvalue(),
                file_name='ocr.zip',
                mime='application/octet-stream',
                # Prevents rerun on click
                on_click="ignore"
            )
else:
    # Clear and reset session
    st.session_state.clear()
    st.cache_data.clear()
    st.stop()