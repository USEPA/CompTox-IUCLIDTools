# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:22:46 2024

@author: VASKO
"""

import src.utils as utils
import pandas as pd
import json
import sys
import pickle

cfg_file = sys.argv[0]


def preprocess_opts(picklist_file, output_dir, norm_tools, fuzz_process, counts):
    print('Performing NLP processing for', picklist_file)
    picklists = pd.read_excel(picklist_file)
    NLP = norm_tools['nlp']
    Lemmatizer = norm_tools['Lemmatizer']

    # loop through picklist fields and save optInfo class for each field
    for field, picklist in picklists.groupby('Field'):
        print(field)
        # set up optInfo class for picklist options
        opts = picklists[(picklists['Field'] == field)].reset_index(drop=True)
        opts['Options'] = opts['Options'].astype(str)

        # Special handling of OHT species notation
        #  (get rid of - [other species] notation)
        if field == 'Species':
            opts['Options'] = opts['Options'].apply(lambda x: x.split(' - ')[0])

        # handle counting, if required
        if counts:
            optInfo = utils.optInfo(opts['Options'], counts=opts['count'])
        else:
            optInfo = utils.optInfo(opts['Options'].drop_duplicates())

        # pull normalized terms / data for each option
        optInfo.get_cuis(NLP, cui_ent_threshold=0.75)
        optInfo.get_lemmas(Lemmatizer, fuzz_process)
        optInfo.get_vectors(NLP)

        field_name = field.replace(':', '')
        with open(f'{output_dir}/{field_name} Info.pkl', 'wb') as fp:
            pickle.dump(optInfo, fp)





