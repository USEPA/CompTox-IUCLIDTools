# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 12:14:22 2024

@author: VASKO
"""

import src.utils as utils
import pandas as pd


def map_by_value_lookup(input_file,
                        input_picklist_file,
                        oht_lookup_fields,
                        num_selections
                        ):
    # Load data
    data = utils.load_data(input_file)

    # Load possible picklist files
    picklist_outname = input_picklist_file.replace('.xlsx', '_fieldnames.xlsx')
    picklist_fields = pd.read_excel(picklist_outname)[0].tolist()

    # Lookup possible input field matches for each of the oht lookup fields
    lookup_results = {}
    if 'Generation' in oht_lookup_fields:
        lookup_results['Generation'] = utils.find_generation_column(
            data[picklist_fields],
            num_selections
        )

    if 'Sex' in oht_lookup_fields:
        lookup_results['Sex'] = utils.find_sex_column(
            data[picklist_fields],
            num_selections
        )

    if 'Effect level (qualifier)' in oht_lookup_fields:
        lookup_results['Effect level (qualifier)'] = utils.find_qualifier_column(
            data[picklist_fields],
            num_selections
        )

    if 'Duration' in oht_lookup_fields:
        lookup_results['Duration'] = utils.find_duration_column(
            data[picklist_fields],
            num_selections
        )

    return (pd.Series(lookup_results))