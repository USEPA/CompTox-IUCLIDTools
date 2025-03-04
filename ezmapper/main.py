# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:53:30 2024

@author: VASKO
"""

import os

from configs.config import config
from src.load_normalizers import load_normalizers
from src.load_matching_params import load_matching_params

from src.preprocess_opts import preprocess_opts
from src.scrape_oht_docx import scrape_oht_docx
from src.scrape_input_df import scrape_input_df
from src.select_field_candidates import select_field_candidates
from src.picklist_field_mapper import map_picklist_fields
from src.record_to_oht_mapper import map_records_to_ohts
from src.picklist_option_mapper import map_picklist_options
from src.numeric_field_mapper import map_numeric_fields
from src.lookup_mapper import map_by_value_lookup
from src.get_field_selections import (get_n_field_selections,
                                      get_top_selection_dict,
                                      merge_selection_dicts
                                      )


def makedir(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        print(f"Warning: {dirname} already exists")


def main(config, user_df):
    # load config params
    update_ohts = config['update_ohts']
    update_input = config['update_input']
    oht_docx_path = config['oht_docx_path']
    oht_picklist_file = config['oht_picklist_file']
    oht_pickle_dir = config['oht_pickle_dir']
    oht_picklist_fields = config['oht_picklist_fields']
    oht_numeric_fields = config['oht_numeric_fields']
    oht_record_fields = config['oht_record_fields']
    oht_other_fields = [f for f in oht_picklist_fields if not f in oht_record_fields]
    oht_dependent_fields = config['oht_dependent_fields']
    oht_lookup_fields = config['oht_lookup_fields']
    oht_data_file = config['oht_data_file']
    oht_data_map_file = config['oht_data_map_file']

    # input_file = config['input_file']
    input_picklist_file = config['input_picklist_file']
    input_numeric_file = config['input_numeric_file']
    input_pickle_dir = config['input_pickle_dir']

    # load normalizer
    norm_tools = load_normalizers()

    # load parameters for fuzzy matching, word vector matching
    match_params = load_matching_params(oht_picklist_fields)

    # make necessary directories
    makedir('output')
    makedir(oht_pickle_dir)
    makedir(input_pickle_dir)

    # process oht forms and save off information for later use
    if update_ohts:
        # pull OHT picklist data from OHT .docx files
        scrape_oht_docx(oht_picklist_fields,
                        oht_docx_path,
                        oht_picklist_file
                        )
        ## NOTE! Manually update `oht_picklist_file` to add a field for
        ##  "Simplified Endpoint" (see example https://usepa.sharepoint.com/:x:/r/sites/ocspp_Work/edsp_chemical_testing/_layouts/15/Doc.aspx?sourcedoc=%7B98121568-D3A4-488B-ADBD-3A3F8FA31D81%7D&file=OHT%20Picklists%20-%20Simple%20Endpoints.xlsx&action=default&mobileredirect=true),
        ##  update `oht_record_fields` in config to replace "Endpoint" with
        ##  "Simplified Endpoint" in order to facilitate record mapping.
        # perform lemmatization, CUI matching, and word vector extraction
        #   on OHT picklist options and save results
        preprocess_opts(oht_picklist_file,
                        oht_pickle_dir,
                        norm_tools,
                        fuzz_process=True,
                        counts=False
                        )

    # process input data and save off information for later use
    if update_input:
        # load in input data file, split picklist vs. numeric fields, and
        #  save to `input_picklist_file` and `input_numeric_file`
        scrape_input_df(user_df,
                        input_picklist_file,
                        input_numeric_file
                        )

        # select picklist field candidates based on preliminary matching to
        #  `oht_picklist_file`
        select_field_candidates(user_df,
                                input_picklist_file,
                                oht_picklist_file,
                                norm_tools
                                )

        # perform lemmatization, CUI matching, and word vector extraction
        #   on input picklist options and save results
        preprocess_opts(input_picklist_file,
                        input_pickle_dir,
                        norm_tools,
                        fuzz_process=True,
                        counts=True
                        )

    # map fields over all OHTs at once, for just record-mapping fields
    map_picklist_fields(user_df,
                        input_picklist_file,
                        input_pickle_dir,
                        oht_pickle_dir,
                        oht_record_fields,
                        match_params
                        )

    # get selections of oht fields
    mapped_fields_records = get_n_field_selections(user_df,
                                                   # input_picklist_file,
                                                   # oht_lookup_fields,
                                                   num_selections=3
                                                   )

    # !! dev note: allow for `mapped_fields_records` to be down-selected by user?
    #    This stop is optional, built in to bypass user selection
    #    dictionary in format {oht_field: [input, fields, selected]} is required
    #    for next steps, however.
    oht_field_dict_records = get_top_selection_dict(mapped_fields_records)

    # map records to oht
    map_records_to_ohts(user_df,
                        input_pickle_dir,
                        oht_pickle_dir,
                        oht_picklist_file,
                        oht_field_dict_records,
                        match_params
                        )

    # --------------------------------------------------------------------------
    # Optional: for this next phase, loop over `input_file`s that have been
    #   filtered to contain records of the same OHT (save as .pkl files)

    # # map fields over just within mapped OHTs, over all remaining fields
    # map_picklist_fields(input_file, ##  !! dev note: update this to restrict to OHT after user corrections, run within OHT
    #                     input_picklist_file,
    #                     input_pickle_dir,
    #                     oht_pickle_dir,
    #                     oht_other_fields,
    #                     match_params
    #                     )
    #
    # # Get selections of oht fields
    # mapped_fields = get_n_field_selections(input_file,
    #                                        num_selections=3
    #                                        )
    #
    #
    # # !! dev note: allow for `mapped_fields` to be down-selected by user?
    # #    This stop is optional, built in to bypass user selection
    # #    dictionary in format {oht_field: [input, fields, selected]} is required
    # #    for next steps, however.
    # oht_field_dict = get_top_selection_dict(mapped_fields)
    #
    # # Combine picklist field mapping dictionaries
    # oht_field_dict_all = merge_selection_dicts(oht_field_dict_records,
    #                                            oht_field_dict
    #                                            )
    #
    # # Map fields set aside for matching by lookup dictionaries
    # mapped_lookup_fields = map_by_value_lookup(input_file,
    #                                            input_picklist_file,
    #                                            oht_lookup_fields,
    #                                            num_selections=3
    #                                            )
    #
    # # !! dev note: allow for `oht_field_dict_lookup` to be down-selected by user?
    # oht_field_dict_lookup = get_top_selection_dict(mapped_lookup_fields)
    # # Optional for picklist fields in lookup:
    # # oht_field_dict_all2 = merge_selection_dicts(oht_field_dict_all,
    # #                                             oht_field_dict_lookup
    # #                                             )
    # # (pass `oht_field_dict_all2` to map_picklist_options)
    #
    #
    # # Map picklist options within a picklist field
    # matched_picklist_options = map_picklist_options(input_file, ## !! dev note: update this to reflect file that denotes OHT in "OHT" column after user corrections
    #                                                 input_pickle_dir,
    #                                                 oht_pickle_dir,
    #                                                 oht_picklist_file,
    #                                                 oht_dependent_fields,
    #                                                 oht_field_dict_all,
    #                                                 match_params
    #                                                 )
    #
    # # Map numeric input fields to matching OHT fields
    # numeric_matches = map_numeric_fields(input_file,
    #                                      input_numeric_file,
    #                                      oht_data_file,
    #                                      oht_data_map_file,
    #                                      oht_numeric_fields
    #                                      )
    #
    # return({
    #     'field_matches_by_lookup': oht_field_dict_lookup,
    #     'picklist_field_matches': oht_field_dict_all,
    #     'picklist_option_matches': matched_picklist_options,
    #     'numeric_field_matches': numeric_matches
    #     })

    field_suggestions = {}
    for oht_field, input_fields in oht_field_dict_records.items():
        for input_field in input_fields:
            field_suggestions[input_field] = oht_field

    return field_suggestions


if __name__ == '__main__':
    main(config)
