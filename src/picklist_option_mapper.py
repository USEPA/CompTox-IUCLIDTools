# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:46:06 2024

@author: VASKO
"""

import src.utils as utils
import pandas as pd
import pickle
from src.scrape_input_df import clean_input_opts


# extract the target match options for one picklist field based on another associated field
#  (used for `get_dual_match` input)
# NOTE: Supports only one dependent field for now
def get_dependent_options(oht_opts1, oht_opts2):
    opts2_dict = {opt: [] for opt in oht_opts1}

    if not any(['other:' in k for k in opts2_dict]):
        opts2_dict['other:'] = []

    for oht_opt in oht_opts2:
        oht_opt1, oht_opt2 = utils.split_text_options(oht_opt)
        if oht_opt1:
            try:
                opts2_dict[oht_opt1].append(oht_opt2)
            except:
                other_key = [k for k in opts2_dict if 'other:' in k][0]
                opts2_dict[other_key].append(oht_opt2)
    return (opts2_dict)


# map input picklist options
def map_picklist_options(input_file,
                         input_pickle_dir,
                         oht_pickle_dir,
                         oht_picklist_file,
                         dependent_fields,
                         oht_field_dict,
                         match_params
                         ):
    # Load data
    data = utils.load_data(input_file)

    # Load picklist file
    oht_picklist = pd.read_excel(oht_picklist_file)

    # Initialize dictionary to store match info
    matched_output = {}
    for oht, dataOHT in data.groupby('OHT'):
        matched_output[oht] = {}

        # Loop through OHT fields and match picklist fields
        for oht_field, input_fields in oht_field_dict.items():
            print('Mapping picklist options for:', oht_field)
            matched_output[oht][oht_field] = {}

            # Set processing in fuzzy matching function
            def fuzz_func(s1, s2):
                return (
                    match_params['fuzz_method'](s1,
                                                s2,
                                                match_params['fuzz_process'][oht_field]
                                                )
                )

            # Load OHT optInfo
            ohtInfo1 = utils.load_optInfo(oht_pickle_dir, oht_field)
            oht_options1 = utils.filter_picklist(oht_picklist, oht, oht_field)
            ohtInfo1 = utils.filter_info(ohtInfo1, oht_options1)

            # Get ToxVal fields that match to OHT field
            for input_field in input_fields:
                print('Input field: ', input_field)

                # Load input optInfo for primary field
                inputInfo1 = utils.load_optInfo(input_pickle_dir, input_field)

                # Get primary input field options to map
                input_dict1 = {
                    'tokens': inputInfo1.opts.tolist(),
                    'cuis': utils.store_opt_info(inputInfo1.opts, inputInfo1.cuis),
                    'lemmas': utils.store_opt_info(inputInfo1.opts, inputInfo1.lemmas),
                    'word_vectors': utils.store_opt_info(inputInfo1.opts, inputInfo1.word_vectors),
                    'counts': utils.store_opt_info(inputInfo1.opts, inputInfo1.counts)
                }

                # Skip dependent fields (account for in dual matching)
                if oht_field in dependent_fields.values():
                    pass

                elif oht_field in dependent_fields:

                    # Get field that depends on primary OHT field
                    dependent_field = dependent_fields[oht_field]
                    matched_output[oht][dependent_field] = {}

                    # Get all OHT options for dependent field
                    ohtInfo2 = utils.load_optInfo(oht_pickle_dir, dependent_field)
                    oht_options2 = utils.filter_picklist(oht_picklist, oht, dependent_field)
                    ohtInfo2 = utils.filter_info(ohtInfo2, oht_options2)

                    # Restrict OHT options for dependent field
                    dependent_dict = get_dependent_options(
                        ohtInfo1.opts,
                        ohtInfo2.opts
                    )

                    # Concatenate paired input info, specific to OHT
                    dependent_input = oht_field_dict[dependent_field][0]  # Supports only one dependent field for now
                    input_pairs = clean_input_opts(dataOHT[[input_field, dependent_input]])

                    # Load input optInfo for dependent field
                    inputInfo2 = utils.load_optInfo(input_pickle_dir, dependent_field)

                    # Get primary input field options to map
                    input_dict2 = {
                        'tokens': inputInfo2.opts.tolist(),
                        'cuis': utils.store_opt_info(inputInfo2.opts, inputInfo2.cuis),
                        'lemmas': utils.store_opt_info(inputInfo2.opts, inputInfo2.lemmas),
                        'word_vectors': utils.store_opt_info(inputInfo2.opts, inputInfo2.word_vectors),
                        'counts': utils.store_opt_info(inputInfo2.opts, inputInfo2.counts)
                    }

                    # Map input options for primary field
                    matches1 = {
                        x: utils.get_single_match(
                            x,
                            input_dict1,
                            ohtInfo1,
                            fuzz_func=fuzz_func,
                            vector_threshold=match_params['vector_thresholds'][oht_field],
                            fuzz_threshold=match_params['fuzz_thresholds'][oht_field]
                        ) for x in input_pairs[input_field].unique()
                    }
                    matched_output[oht][oht_field][input_field] = matches1

                    # Match toxval options to OHT options for primary and dependent fields
                    matched_output[oht][dependent_field][dependent_input] = {
                        x[dependent_input]: utils.get_dual_match(
                            x,
                            matches1[x[input_field]],
                            dependent_input,
                            input_dict2,
                            ohtInfo2,
                            dependent_dict,
                            fuzz_func=fuzz_func,
                            vector_threshold=match_params['vector_thresholds'][oht_field],
                            fuzz_threshold=match_params['fuzz_thresholds'][oht_field]
                        ) for _, x in input_pairs.iterrows()
                    }

                else:
                    # Get opt info, specific to OHT
                    input_opts = clean_input_opts(dataOHT[input_field])

                    # Match toxval options to OHT options
                    matched_output[oht][oht_field][input_field] = {
                        x: utils.get_single_match(
                            x,
                            input_dict1,
                            ohtInfo1,
                            fuzz_func=fuzz_func,
                            vector_threshold=match_params['vector_thresholds'][oht_field],
                            fuzz_threshold=match_params['fuzz_thresholds'][oht_field]
                        ) for x in input_opts[input_field].unique()
                    }

    with open(input_file.replace('.xlsx', '_matched_picklist_options.pkl'), 'wb') as fp:
        pickle.dump(matched_output, fp)

    return (matched_output)
