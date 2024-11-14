# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:12:22 2024

@author: VASKO
"""
import os
import sys

import numpy as np
import pandas as pd

import src.utils as utils
import pickle
import getpass

user = getpass.getuser()


def map_picklist_fields(user_df,
                        input_picklist_file,
                        input_pickle_dir,
                        oht_pickle_dir,
                        oht_fields,
                        match_params
                        ):
    print('Mapping picklist fields for:\n', '\n'.join(oht_fields))

    # Set processing in fuzzy matching function
    def fuzz_func(s1, s2):
        return (
            match_params['fuzz_method'](s1,
                                        s2,
                                        match_params['fuzz_process'][oht_field]
                                        )
        )

    # Loop through potential input fields and log info
    input_fields = pd.read_excel(input_picklist_file)
    input_dict = {}
    for input_field, _ in input_fields.groupby('Field'):
        inputInfo = utils.load_optInfo(input_pickle_dir, input_field)
        input_dict[input_field] = {
            'tokens': inputInfo.opts.tolist(),
            'cuis': utils.store_opt_info(inputInfo.opts, inputInfo.cuis),
            'lemmas': utils.store_opt_info(inputInfo.opts, inputInfo.lemmas),
            'word_vectors': utils.store_opt_info(inputInfo.opts, inputInfo.word_vectors),
            'counts': utils.store_opt_info(inputInfo.opts, inputInfo.counts)
        }

    # Load toxval candidates for each oht of interest
    fname = input_picklist_file.replace('.xlsx', '_candidates') + '.pkl'
    with open(fname, 'rb') as fp:
        candidates = pickle.load(fp)
    candidates = {f: c for f, c in candidates.items() if f in oht_fields}

    # Run through OHTs, attempt fuzzy-matching of picklist options to inputVal
    input_values = {}
    input_matched = {}
    product_dict = {}

    for oht_field, input_candidates in candidates.items():
        print(oht_field)

        # Load optInfo dict from prior processing
        ohtInfo = utils.load_optInfo(oht_pickle_dir, oht_field)

        input_values[oht_field] = {}
        input_matched[oht_field] = {}
        product_dict[oht_field] = {}
        for input_field in input_candidates:
            print('Calculating fuzzy matches for:' + input_field)
            matches = [
                utils.get_single_match(
                    x,
                    input_dict[input_field],
                    ohtInfo,
                    fuzz_func=fuzz_func,
                    vector_threshold=match_params['vector_thresholds'][oht_field],
                    fuzz_threshold=match_params['fuzz_thresholds'][oht_field]
                )
                for x in input_dict[input_field]['tokens']
            ]

            matches = pd.Series(matches)
            values = matches.apply(utils.get_match_values)

            input_values[oht_field][input_field] = values
            input_matched[oht_field][input_field] = pd.Series(
                t for t, v in zip(input_dict[input_field]['tokens'], values) if not v == ''
            )

            # -- Calculate proportions of overlap in fuzzy matching
            oht_props = ohtInfo.opts.isin(
                values.unique().tolist()
            ).value_counts(normalize=True)
            input_props = utils.get_prop_matched(
                input_matched[oht_field][input_field],
                input_dict[input_field]['counts']
            )
            product_dict[oht_field]
            if True in oht_props and True in input_props:
                product_dict[oht_field][input_field] = oht_props[True] * input_props[True]

    outname = 'output/product_dict.pkl'
    with open(outname, 'wb') as fp:
        pickle.dump(product_dict, fp)
