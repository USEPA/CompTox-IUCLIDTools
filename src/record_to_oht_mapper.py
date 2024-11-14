# -*- coding: utf-8 -*-
"""
Created on Tue May 14 12:16:31 2024

@author: VASKO
"""

import pandas as pd
import pickle
import getpass
import src.utils as utils
from src.scrape_input_df import drop_text

user = getpass.getuser()


def map_to_business_rule(series, matches_dict, input_to_rule_map):
    rule = input_to_rule_map[series.name]
    return (
        series.apply(lookup_toxmatch, args=(matches_dict[rule],))
    )


def lookup_toxmatch(toxmatch, matches):
    rule_matches = matches[matches['tox match'] == toxmatch]['Rule Value']
    if len(rule_matches) > 0:
        rule_match = rule_matches.iloc[0]
        if len(rule_match) > 0:
            return (rule_match[0])
        else:
            return (None)
    else:
        return (None)


# make a dictionary specifying which OHTs are possible for each picklist option
def compile_mapping_rules(oht_picklist_file, oht_field_dict):
    map_rules = pd.read_excel(oht_picklist_file)
    map_rules = map_rules[map_rules['Field'].isin(oht_field_dict)].reset_index()
    map_rules['Options'] = map_rules['Options'].apply(
        lambda x: x.split(' - ')[0]
    )
    map_equal = {rule_field: {} for rule_field in oht_field_dict}
    for rule_field in oht_field_dict:
        mask1 = map_rules['Field'] == rule_field
        map_rule = map_rules[mask1].drop_duplicates([
            'OHT',
            'Options'
        ])
        map_rule = map_rule[['OHT', 'Options']]
        map_collapse = map_rule.groupby('Options').agg(list)
        map_equal[rule_field] = {
            val: x['OHT'] for val, x in map_collapse.iterrows()
        }
    return (map_equal)


def map_records_to_ohts(user_df,
                        input_pickle_dir,
                        oht_pickle_dir,
                        oht_picklist_file,
                        oht_field_dict,
                        match_params
                        ):
    print('Matching records to their OHTs')

    # load data
    # data = utils.load_data(input_file)

    # join input fields that both map to an OHT field
    reduced_fields = []
    oht_field_dict2 = {}
    for oht_field, input_fields in oht_field_dict.items():
        new_name = '_'.join(input_fields)
        user_df[new_name] = user_df[input_fields].astype(str).apply(' '.join, axis=1)
        reduced_fields.append(new_name)
        oht_field_dict2[oht_field] = new_name

    # subset data to fields relevant for mapping
    user_df = user_df[reduced_fields].drop_duplicates().reset_index(drop=True)
    for field in reduced_fields:
        user_df[field] = drop_text(user_df[field].astype(str), 'other')
        user_df[field] = user_df[field].str.lower()

    # organize mapping rules into dictionary
    map_equal = compile_mapping_rules(oht_picklist_file, oht_field_dict2)

    # loop through records and map to OHT options in map rules
    matches_dict = {}
    for rule_field, input_field in oht_field_dict2.items():
        # Set processing in fuzzy matching function
        def fuzz_func(s1, s2):
            return (
                match_params['fuzz_method'](s1,
                                            s2,
                                            match_params['fuzz_process'][rule_field]
                                            )
            )

        # Load OHT optInfo
        ohtInfo = utils.load_optInfo(oht_pickle_dir, rule_field)

        # Load input optInfo
        inputInfo = utils.load_optInfo(input_pickle_dir, input_field)
        input_dict = {
            'tokens': inputInfo.opts.tolist(),
            'cuis': utils.store_opt_info(inputInfo.opts, inputInfo.cuis),
            'lemmas': utils.store_opt_info(inputInfo.opts, inputInfo.lemmas),
            'word_vectors': utils.store_opt_info(inputInfo.opts, inputInfo.word_vectors),
            'counts': utils.store_opt_info(inputInfo.opts, inputInfo.counts)
        }

        # get matches
        matches = [
            utils.get_single_match(token,
                                   input_dict,
                                   ohtInfo,
                                   fuzz_func=fuzz_func,
                                   vector_threshold=match_params['vector_thresholds'][rule_field],
                                   fuzz_threshold=match_params['fuzz_thresholds'][rule_field]
                                   )
            for token in input_dict['tokens']
        ]

        # store matches in dataframe, then in dictionary according to rule
        matches = pd.DataFrame(matches)
        matches['tox match'] = input_dict['tokens']
        matches.columns = ['Rule Value', 'Match Type', 'Score', 'tox match']
        matches_dict[rule_field] = matches[['tox match', 'Rule Value', 'Match Type', 'Score']]

    # flip oht dictionary, key by input field instead of oht field
    input_to_rule_map = {inp: oht for oht, inp in oht_field_dict2.items()}

    # transform matches dataframe
    matched_df = user_df[input_to_rule_map.keys()].apply(
        map_to_business_rule,
        args=(matches_dict, input_to_rule_map), axis=0
    )
    matched_df = matched_df.rename(columns=input_to_rule_map)
    matched_df = pd.concat([user_df, matched_df], axis=1)

    for rule_field, rule_match in map_equal.items():
        matched_df['OHTs_' + rule_field] = matched_df[rule_field].map(rule_match)

    oht_columns = ['OHTs_' + rule_field for rule_field in map_equal]
    matched_df[oht_columns] = matched_df[oht_columns].fillna('')
    print(matched_df.columns)
    matched_df['OHT_Final'] = matched_df.apply(
        # lambda x: set(x['OHTs_Endpoint']) & set(x['OHTs_Route of administration']) & set(x['OHTs_Species']),
        lambda x: set(x['OHTs_Route of administration']) & set(x['OHTs_Species']),

        axis=1
    )

    matched_df['OHT_Final'] = matched_df['OHT_Final'].apply(list)

    outname = 'output/record_matches.pkl'
    with open(outname, 'wb') as fp:
        pickle.dump(matched_df, fp)
    print('Exporting matching assignments to: ', outname)
