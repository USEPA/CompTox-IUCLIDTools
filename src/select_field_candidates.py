# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:17:53 2024

@author: VASKO
"""

import pickle
import src.utils as utils
import pandas as pd


def count_tokens(opts, tokenizer):
    counts = utils.count_values(pd.Series(opts))
    return (utils.get_token_counts(counts, tokenizer))


# pull the fields with the top 10 scores
def get_top_10(ratio_dict):
    s = pd.Series(ratio_dict)
    return (utils.top_n(s, n=10))


def select_field_candidates(user_df,
                            input_picklist_file,
                            oht_picklist_file,
                            norm_tools
                            ):
    # Load input data
    # data = utils.load_data(input_file)

    # Load input picklist field options
    input_picklist_fields = pd.read_excel(input_picklist_file)

    # Load OHT picklist into
    oht_picklists = pd.read_excel(oht_picklist_file)

    # Get token counts across OHTs
    oht_tokens = {}
    for oht_field, oht_options in oht_picklists.groupby('Field'):
        oht_tokens[oht_field] = count_tokens(oht_options['Options'],
                                             norm_tools['tokenizer']
                                             )

    # Get token counts across input
    input_tokens = {}
    for input_field in input_picklist_fields['Field'].unique():
        input_tokens[input_field] = count_tokens(user_df[input_field],
                                                 norm_tools['tokenizer']
                                                 )

    # Compare token distributions and scale by average field sizes
    candidates = {}
    print('Selecting Candidates for:')
    for oht_field, oht_df in oht_tokens.items():
        print('OHT Field:', oht_field)
        candidates[oht_field] = []
        input_oht_ratio = {}
        oht_input_ratio = {}

        for input_field, input_df in input_tokens.items():

            # # Calculate basic statistics to generate field matching candidates
            # input_data = data[input_field].dropna().astype(str)
            # oht_data = oht_picklists[oht_picklists['Field'] == oht_field]['Options']

            # Compare relative lengths of input and oht picklist options (for now, IGNORE results)
            len_ratio = min(
                input_df['index'].apply(len).mean() / oht_df['index'].apply(len).mean(),
                oht_df['index'].apply(len).mean() / input_df['index'].apply(len).mean()
            )

            # Compare the relative number of unique options (for now, IGNORE results)
            opt_ratio = min(
                input_df['index'].nunique() / oht_df['index'].nunique(),
                oht_df['index'].nunique() / input_df['index'].nunique()
            )
            try:
                na_ratio = user_df[input_field].isna().value_counts(normalize=True)[False]
            except KeyError:
                na_ratio = 0

            # Get dataframes of only overlapping values
            oht2 = oht_df[oht_df['index'].isin(
                input_df['index'])].sort_values(by='index')
            inp2 = input_df[input_df['index'].isin(
                oht_df['index'])].sort_values(by='index')

            # look for any tokens to overlap between input and oht fields
            if any(inp2['index'].isin(oht2['index'])):
                if len_ratio > 0 and opt_ratio > 0 and na_ratio > 0:
                    # candidates[oht_field].append(input_field)

                    # Record proportion of overlapping tokens
                    input_oht_ratio[input_field] = input_df['index'].isin(
                        oht_df['index']
                    ).mean()
                    oht_input_ratio[input_field] = oht_df['index'].isin(
                        input_df['index']
                    ).mean()

        # take the top 10 input fields with overlap for input and ohts
        top_input_oht = get_top_10(input_oht_ratio)
        top_oht_input = get_top_10(oht_input_ratio)

        # select the fields that were in the top 10 of overlap for both input and OHTs
        candidates[oht_field] = set(top_input_oht) & set(top_oht_input)

    print('candidates:')
    print(candidates)

    # # Get candidates, independent of associated OHT
    # input_field_candidates = []
    # for _, input_fields in candidates.items():
    #     input_field_candidates += list(input_fields)
    # input_field_candidates = list(set(input_field_candidates))
    #
    # # Reduce the input picklist field options to just those in candidates
    # reduced_picklist_fields = input_picklist_fields[
    #     input_picklist_fields['Field'].isin(input_field_candidates)
    #     ]
    #
    # # Overwrite the input picklist field options file
    # reduced_picklist_fields.to_excel(input_picklist_file)
    # print('Re-saving reduced picklist field data: ', input_picklist_file)

    # Save candidate info to file
    fname = input_picklist_file.replace('.xlsx', '_candidates') + '.pkl'
    with open(fname, 'wb') as fp:
        pickle.dump(candidates, fp)
    print('Saving candidate lists to: ', fname)
