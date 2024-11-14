# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:25:42 2024

@author: VASKO
"""

import copy
import pickle
import pandas as pd
import src.utils as utils


def get_n_field_selections(user_df, num_selections):
    # load matching scores from `map_picklist_fields()`
    product_dict_file = 'output/product_dict.pkl'
    with open(product_dict_file, 'rb') as fp:
        map_dict = pickle.load(fp)

    # pull input fields with top `num_selections` scores for each oht
    map_df = pd.DataFrame(map_dict)
    mapped_fields = map_df.apply(utils.top_n, n=num_selections, axis=0)

    return (mapped_fields)


def get_top_selection_dict(mapped_fields):
    # assumes `mapped_fields` is sorted by top scoring input field
    selection_dict = {}
    for f, fields in mapped_fields.items():
        selection_dict[f] = [fields[0]]
    return (selection_dict)


# merge two outputs from `get_top_selection_dict`
def merge_selection_dicts(d1, d2):
    d3 = copy.deepcopy(d1)
    d3.update(d2)
    return (d3)
