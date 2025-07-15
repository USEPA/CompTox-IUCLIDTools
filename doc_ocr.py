# %%
# Packages used as part of this script.  Package versions can be found as part of the README.
# import io
import argparse
import warnings
import os
import re
import json
import pandas as pd
import math

# from collections import defaultdict
# from pathlib import Path
# from typing import List, Optional
from multiprocessing import Pool

import fitz
# import torch
import PyPDF2
from suffix_tree import Tree

from PIL import Image
# from tqdm.notebook import tqdm
from tqdm import tqdm
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

# Parallel processing
import contextlib
import joblib
from joblib import Parallel, delayed

# Turn off warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Define helper functions
def jsonParser(json_res: json):
    """ 
    Parse the json result of OCR into a text file matching the format, with new line characters to split lines and pages. 
    Args:
        json_res (json): json of OCR results
    Returns:
        str: string of OCR output split by pages
    """
    # Unpack json into str
    text = ""
    for page in json_res['pages']:
        text = text + "PAGE: " + str(page['page_idx'] + 1) + "\n\n"
        for block in page['blocks']:
            for line in block['lines']:
                for word in line['words']:
                    text = text + word['value'] + " "
                text = text + "\n"
    return(text)

def jsonPreds(json: json, f: str, path:str):
    """ 
    Parse the json result of OCR into a table for investigating confidence levels of predictions. To be used for typo correction.
    Args:
        json (json): json OCR results
        f (str): file name
        path (str): path to save 
    Returns:
        Creates excel file of confidence levels at filepath
    """
    filepath = path + "/predictions/" + f + ".xlsx"

    # Unpack json into prediction and confidence for every word
    result = ""
    for page in json['pages']:
        for block in page['blocks']:
            for line in block['lines']:
                for word in line['words']:
                    if result == "" :
                        result = [[word['value'],word['confidence']]]
                    else: 
                        result.append([word['value'], word['confidence']])
    # If not blank, export to excel
    if result != "":
        df = pd.DataFrame(result,columns=["Prediction","Confidence"])
        df.to_excel(filepath)

def get_doc_page_count(filepath):
    """
    Try to open input PDF file and get the number of pages.

    Args:
        filepath (str): Filepath of file to open.

    Returns:
        num: Numeric number of pages in the PDF file.
    """
    # Try to open file
    try:
        file = open(filepath, 'rb')
        pdf = PyPDF2.PdfReader(file)
        # If can open, save page number
        page_n = len(pdf.pages)
    # If cannot open, print error so problem can be identified
    except Exception:
        print("Opening error: " + os.path.basename(filepath))
        page_n = 0
    
    return page_n

def write_output_file(filepath, contents):
    """
    Write output file for input contents and with input filepath.

    Args:
        filepath (str): Filepath to write file to.
        contents (str): File contents.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(contents)
    except Exception:
        print("Encoding error: " + os.path.basename(filepath))

def prep_docs(in_doc_dir, ocr_text_path):
    """
    Prepare dataframe of file information for the OCR workflow. 
    Includes filtering out already completed documents and preparing file and filepaths
    for input and output files.

    Args:
        in_doc_dir (str): Parent file directory of input files to process.
        ocr_text_path (str): File directory for OCR text files to be written.

    Returns:
        pd.DataFrame: Dataframe with prepared filepaths and filenames.
    """
    # List files in input directory
    basefiles = os.listdir(in_doc_dir)
    # Filter to PDF files
    basefiles = [f for f in basefiles if f.lower().endswith('.pdf')]
    
    # Look at results already processed (flagged with "_EMBEDDED" and "_OCR")
    # completed_files = [f.replace("_EMBEDDED", "").replace("_OCR", "") for f in os.listdir(ocr_text_path)]
    # Replace multiple suffix strings from completed file list
    # https://gist.github.com/bgusach/a967e0587d6e01e889fd1d776c5f3729
    # Replacements could grow to many suffixes as development continues, so making more dynamic
    # and not just adding more .replace() arguments to the end...
    replacements = {"_EMBEDDED":"", "_OCR": "", ".txt": ".pdf"}
    replacements = {key: val for key, val in replacements.items()}
    
    # Place longer ones first to keep shorter substrings from matching where the longer ones should take place
    # For instance given the replacements {'ab': 'AB', 'abc': 'ABC'} against the string 'hey abc', it should produce
    # 'hey ABC' and not 'hey ABc'
    rep_sorted = sorted(replacements, key=len, reverse=True)
    rep_escaped = map(re.escape, rep_sorted)
    
    # Create a big OR regex that matches any of the substrings to replace
    pattern = re.compile("|".join(rep_escaped))
    
    # For each match, look up the new string in the replacements, being the key the normalized old string
    completed_files = [pattern.sub(lambda match: replacements[match.group(0)], f) 
                       for f in os.listdir(ocr_text_path)]

    # Get list of files to process
    todo_files = [f for f in basefiles if f.lower() not in [x.lower() for x in completed_files]]

    # No files to process
    if len(todo_files) == 0:
        return pd.DataFrame()
    
    # Create dataframe to track all file processing metadata
    files_df = pd.DataFrame(todo_files, columns=['filename'])
    files_df['in_filepath'] = files_df.apply(lambda row: os.path.join(in_doc_dir, row['filename']), axis=1)
    # Default path to "EMBEDDED tag"
    # files_df['ocr_text_filepath'] = files_df.apply(lambda row: os.path.join(ocr_text_path, row['filename'].replace(".pdf", "_EMBEDDED.txt")), axis=1)
    files_df['ocr_text_filepath'] = files_df.apply(lambda row: os.path.join(ocr_text_path, 
                                                                            re.sub(".pdf", "_EMBEDDED.txt", row['filename'], 
                                                                                   flags=re.IGNORECASE)), axis=1)
    # Check if documents can be opened, if can save page number into vector.
    files_df['page_vector'] = files_df.apply(lambda row: get_doc_page_count(row['in_filepath']), axis=1)
    # Filter out documents with 0 pages
    # Sort by page number ascending
    files_df = files_df[files_df['page_vector'] > 0].sort_values(by='page_vector')
    # Set default as does not need OCR
    files_df['OCR_queue'] = False

    return files_df.reset_index(drop=True)

def extract_doc_text_layer(files_df):
    """
    Attempt to extract the text layer from an input PDF. Modify the input
    files_df dataframe to add new OCR_queue field flag for if file needs OCR.

    Args:
        files_df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: Modified input dataframe with new OCR_queue field.
    """
    # Identify and extract embedded text layers
    for i in tqdm(files_df.index):
        f = files_df.loc[i,'filename']
        in_filepath = files_df.loc[i, 'in_filepath']
        page_n = files_df.loc[i, 'page_vector']
        ocr_text_filepath = files_df.loc[i, 'ocr_text_filepath']
        text = ""
        # Try to pull out the embedded text layer.
        try:
            with fitz.open(in_filepath) as doc:
                for j in range(page_n):
                    page = doc[j]
                    temptext = "PAGE: " + str(page.number + 1) + "\n" + page.get_text()
                    text += temptext
        # If anything goes wrong here, clearly want to send it to OCR.
        except Exception:
            print("File Opening error: " + f)
            files_df.loc[i, 'OCR_queue'] = True
            continue
        # Need to filter out "bad" embedded text layers.  If there's less than 50 characters per page, it's almost certainly bad.
        if len(text) < 50*page_n:
            files_df.loc[i, 'OCR_queue'] = True
            continue
        
        # Use suffix tree
        # Computer based additions to manually scanned documents are usually headers and footers added to the entire document.  
        tree = Tree()
        tree.add(1,text)
        # From the suffix trees, we can pull the list of substrings for any given character length that repeat the most time - the maximal repeats.
        # If a header/footer addition has occurred, the header/footer should be a maximal repeat across the entire string - because it likely is
        # the entire string.  Pull out the maximal repeats, and if we can't, then send to OCR.
        try:
            maximal_repeats = tree.maximal_repeats()
        except:
            files_df.loc[i, 'OCR_queue'] = True
            continue
        # Only care about substrings that are long enough, to ensure we don't scan out, for example, a table of data filled with a ton of "NA"s.  
        # Identify how many of these substrings are possible based on the length of the substring.  If the number of them is enough to be at least
        # 20% of the total string, better to send it to OCR to be safe.
        for id, path in maximal_repeats:
            if len(path) > 10:
                poss = len(text)/len(path)
                tempstr = ""
                for j in range(0,len(path)):
                    tempstr = tempstr + path[j]
                if text.count(tempstr) > poss/5:
                    files_df.loc[i, 'OCR_queue'] = True
                    continue

        # If these things aren't concerns save text layer in same format
        # Flagged as _EMBEDDED to make it clear it comes from an embedded text layer for tracking purposes.
        write_output_file(ocr_text_filepath, text)
    
    return files_df

def doc_ocr(files_df):
    """
    Perform OCR on input filesfiles.

    Args:
        files_df (pd.DataFrame): Input dataframe of files to perform OCR on.

    Returns:
        pd.DataFrame: Modified input dataframe filtered to files that were OCR processed.
    """

    # Run OCR using docTR for those without a text layer
    # Use db_resnet50 encorder and crnn_mobilenet_v3_large decoder, have been chosen based on benchmark testing for 3M docuset
    model = ocr_predictor('db_resnet50', 'crnn_mobilenet_v3_large', pretrained=True, assume_straight_pages=False)
    # Filter out those that do not need OCR
    files_df = files_df[files_df['OCR_queue'] == True]
    # Prep OCR text filepath flag
    files_df['ocr_text_filepath'] = files_df['ocr_text_filepath'].str.replace('_EMBEDDED.txt', '_OCR.txt')
    for i in tqdm(files_df.index):
        in_filepath = files_df.loc[i, 'in_filepath']
        ocr_text_filepath = files_df.loc[i, 'ocr_text_filepath']
        
        # Open doc and perform OCR
        doc = DocumentFile.from_pdf(in_filepath)
        result = model(doc)
        json_res = result.export()
        text = jsonParser(json_res)

        write_output_file(ocr_text_filepath, text)
        
        # And a step at the end to save predictions, currently commented out due to the fact that typo correction is not complete.
        # jsonPreds(json_res, f, ocr_text_path)
    
    return files_df

def doc_embed_ocr(embedfiles, in_doc_dir, ocr_text_path, embedpath):
    """
    Embed the OCR text as a text layer in a new PDF.

    Args:
        embedfiles (list): List of filenames of PDFs to add text layer to.
        in_doc_dir (str): Parent file directory of input files to process.
        ocr_text_path (str): File directory for OCR text files to be written.
        embedpath (str): File directory to save new PDFs with text layers embedded.

    Returns:
        None. PDF files are created with text layers and saved to the emdbedpath directory.
    """
    
    for i in tqdm(range(len(embedfiles))):
        f = os.path.basename(embedfiles[i])
        in_filepath = os.path.join(in_doc_dir, embedfiles[i])
        ocr_filepath = os.path.join(ocr_text_path, embedfiles[i].replace('.pdf', '_OCR.txt'))
        # Get text from OCR file
        with open(ocr_filepath, 'r') as file:
            text = file.read()
        page_pattern = r"PAGE\: \d+\n"
        embedtext = re.split(page_pattern, text)[1:]

        # Try to embed the OCR extracted text for each page
        try:
            doc = fitz.open(in_filepath)
            for page in doc:
                ocr_page = embedtext[page.number]
                tw = fitz.TextWriter(page.rect)

                start_x = start_y = 72
                line_spacing = 14
                font_size = 12

                y = start_y
                for line in ocr_page.splitlines():
                    if line:
                        tw.append(
                            pos=(start_x, y),
                            text=line,
                            fontsize=font_size
                        )
                        y += line_spacing
                
                tw.write_text(page, render_mode=3)

            embedfile = os.path.join(embedpath, f)
            doc.save(embedfile)
        except:
            print(f"{in_filepath}: Embed Error")

def get_cmd_args():
    """
    Create command line argument parser.

    Returns:
        argparse.ArgumentParser: Parser with arguments to handle from command line.
    """
    parser = argparse.ArgumentParser(description="A script that processes user input.")
    # Add parser arguments
    parser.add_argument("--in_doc_dir", 
                        type = str, 
                        required = False,
                        default = "input_docs",
                        help = "Parent file directory of input files to process. Default 'input_docs'")
    parser.add_argument("--ocr_text_path", 
                        type = str, 
                        required = False,
                        default = "input_docs_text",
                        help="File directory for OCR text files to be written. Default 'input_docs_text'")
    parser.add_argument("--embedpath", 
                        type = str, 
                        required = False,
                        default = "input_docs_embedded",
                        help = "Required if --embed_ocr is True, file directory to save new PDFs with text layers embedded. Default 'input_docs_embedded'")
    parser.add_argument("--embed_ocr", 
                        type = bool, 
                        required = False,
                        default = True,
                        help = "Optional boolean whether to embed OCR text layers in new PDF (Default True)")

    return parser

def run_ocr(files_df, embedpath, embed_ocr):
    """
    Orchestrate the full OCR run

    Args:
        files_df (_type_): _description_
        embedpath (_type_): _description_
        embed_ocr (_type_): _description_
    """
    
    print(f"Extracting available text layers...Process ID {os.getpid()}")
    files_df = extract_doc_text_layer(files_df)
    print("OCR for those without text layers...")
    files_df = doc_ocr(files_df)

    if embed_ocr:
        # Check if exist, if not make it
        if not os.path.isdir(embed_ocr):
            os.makedirs(embedpath, exist_ok=True)
        embedfiles = os.listdir(embedpath)
        ocr_text = [f.replace('_OCR.txt', '.pdf') for f in os.listdir(ocr_text_path) if '_OCR.txt' in f]
        embedfiles_todo = [f for f in ocr_text if f not in embedfiles]
        if len(embedfiles_todo):
            print("Embedding OCR into new PDF files...")
            doc_embed_ocr(embedfiles = embedfiles_todo, 
                          in_doc_dir = in_doc_dir, 
                          ocr_text_path = ocr_text_path,
                          embedpath = embedpath)
        else:
            print("...No new documents to embed...")
    print("Done.")

# https://stackoverflow.com/questions/24983493/tracking-progress-of-joblib-parallel-execution/58936697#58936697
@contextlib.contextmanager
def tqdm_joblib(tqdm_object):
    """Context manager to patch joblib to report into tqdm progress bar given as argument"""
    class TqdmBatchCompletionCallBack(joblib.parallel.BatchCompletionCallBack):
        def __call__(self, *args, **kwargs):
            tqdm_object.update(n=self.batch_size)
            return super().__call__(*args, **kwargs)

    old_batch_callback = joblib.parallel.BatchCompletionCallBack
    joblib.parallel.BatchCompletionCallBack = TqdmBatchCompletionCallBack
    try:
        yield tqdm_object
    finally:
        joblib.parallel.BatchCompletionCallBack = old_batch_callback
        tqdm_object.close()

# %%
if __name__ == "__main__":
    # Get and parse arguments
    args = get_cmd_args()
    args = args.parse_args()
    # Identify directory for files
    in_doc_dir = args.in_doc_dir # 'input_docs'
    # Identify directory for text layer 
    ocr_text_path = args.ocr_text_path # 'input_docs_text'
    # Identify directory for embedded files
    embedpath = args.embedpath # 'input_docs_embedded'
    # Boolean to embed OCR's text into new file or not
    embed_ocr = args.embed_ocr # True
    
    print("Preparing documents...")
    # Check if output directory exists, if not make it
    if not os.path.isdir(ocr_text_path):
        os.makedirs(ocr_text_path, exist_ok=True)
    
    files_df = prep_docs(in_doc_dir, ocr_text_path)
    
    if not files_df.empty:
        # Get number of cores
        num_logical_cores = joblib.cpu_count()
        # Run the OCR in parallel
        with tqdm_joblib(tqdm(desc="OCR Parallel", total=len(files_df.index))) as progress_bar:
            # Run in parallel using 25% of available cores
            Parallel(n_jobs=math.floor(num_logical_cores*0.25))(delayed(run_ocr)(files_df=files_df.iloc[[i]], 
                                                 embedpath=embedpath, 
                                                 embed_ocr=embed_ocr) 
                                                 for i in files_df.index)
        # # Run serial
        # for i in tqdm(files_df.index):
        #     # Process each file individually
        #     run_ocr(files_df=files_df.iloc[[i]], 
        #             embedpath=embedpath, 
        #             embed_ocr=embed_ocr)
    else:
        print("...No new document text layers to extract...")

    
