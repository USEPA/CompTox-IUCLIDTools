# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 07:44:30 2024

@author: VASKO
"""

import pandas as pd
from docx.api import Document
import regex as re
import pickle
import os


def get_oht_from_file(filename):
    try:
        oht_match = re.match(r'^OHT (\d+(?:-\d+)?) -', filename)
        if oht_match:
            print(oht_match)
            oht_num = oht_match.group(1)
            print(oht_num)
            return (oht_num)
        else:
            print('No match found')
            return None
    except TypeError:
        oht_match = re.match('^OHT [0-9]{2}', filename)
        print(oht_match)
        oht_num = oht_match[0].split(' ')[-1]
        try:
            return (oht_num)
        except TypeError:
            return (None)


def clean_picklist_options(text):
    print(text)
    opts = text.split('\n- ')
    print(opts)
    opts = [opt for opt in opts if not opt[-1] == ':']
    opts = [opt.lower() for opt in opts]
    opts = list(set(opts))
    return (opts)


## !! TODO: abbreviation detection?


# -- Loop through all OHT forms and pull picklist options
def scrape_oht_docx(oht_fields, oht_docx_path, oht_picklist_file):
    oht_files = [f for f in os.listdir(oht_docx_path) if 'ENDPOINT_STUDY_RECORD' in f]
    picklist_options = {}
    for oht_file in oht_files:
        print(oht_file)
        oht = get_oht_from_file(oht_file)

        picklist_options[oht] = {}

        document = Document(f'{oht_docx_path}/{oht_file}')
        table = document.tables[0]

        keys = None
        for oht_field in oht_fields:
            print(oht_field)
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)

                if i == 0:
                    keys = tuple(text)
                    continue
                row_data = dict(zip(keys, text))
                if row_data['Field name\n'] == oht_field:
                    picklist_data = row_data['Picklist\nFreetext template']
                    try:
                        picklist_options[oht][oht_field] = clean_picklist_options(
                            picklist_data
                        )
                    except:
                        break
                    break

    picklist_df = pd.DataFrame(picklist_options).transpose()
    picklist_df = picklist_df.reset_index(names='OHT')
    picklist_long = picklist_df.melt(
        id_vars='OHT',
        var_name='Field',
        value_name='Options'
    )
    picklist_out = picklist_long.explode('Options').dropna()
    picklist_out.to_excel(oht_picklist_file, index=False)

