import streamlit as st
import subprocess
import sys
import os

# Session variables
if "ocr_doc_file_paths" not in st.session_state:
    st.session_state["ocr_doc_file_paths"] = []

# Set the title and description of the web app
st.title("EZ Mapper")
st.markdown("A tool for mapping and transforming data to an i6z file.")

# Create a sidebar for user inputs
st.sidebar.title("Upload File")
uploaded_files = st.sidebar.file_uploader("Choose a PDF file", 
                                         type=["pdf"], 
                                         accept_multiple_files=True)


if len(uploaded_files) > 0:
    # subprocess.run([f"{sys.executable}", "script.py"])
    in_doc_dir = 'output/ocr_docs'
    ocr_text_path = 'output/ocr_text'
    ocr_cmd = [
            ".ocr_venv/Scripts/python.exe",
            "doc_ocr.py",
            '--in_doc_dir',
            in_doc_dir,
            '--ocr_text_path',
            ocr_text_path
            ]

    # Write uploaded files to in_doc_dir
    for f in uploaded_files:
        # Create file paths for OCR process
        file_path = os.path.join(in_doc_dir, f.name)
        ocr_text_path_em = os.path.join(ocr_text_path, f.name.replace(".pdf", "_EMBEDDED.txt"))
        ocr_text_path_ocr = os.path.join(ocr_text_path, f.name.replace(".pdf", "_OCR.txt"))
        # Add to session state to clean up later
        st.session_state["ocr_doc_file_paths"].append(file_path)
        st.session_state["ocr_doc_file_paths"].append(ocr_text_path_em)
        st.session_state["ocr_doc_file_paths"].append(ocr_text_path_ocr)
        # Write input PDF to file
        with open(file_path, "wb") as ff:
            ff.write(f.getbuffer())

    # Display terminal output
    # Run the OCR script
    # https://discuss.streamlit.io/t/redirecting-terminal-output/56763
    try:
        result = subprocess.Popen(ocr_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        print(stdout)
        print(stderr)
        # Display the terminal output
        st.title("Display console output:")
        st.write('\n'.join(stdout.decode().split('\n')[1:][:-1]))
    except FileNotFoundError:
        print("Error: Command not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
else:
    # Remove temporary OCR files
    if len(st.session_state["ocr_doc_file_paths"]) > 0:
        print("Deleting temp OCR docs")
        for f in st.session_state["ocr_doc_file_paths"]:
            if len(f) > 0 and os.path.exists(f):
                print(f"...Deleting file {f}")
                os.remove(f)
                
        # Reset after deleting
        st.session_state["ocr_doc_file_paths"] = []