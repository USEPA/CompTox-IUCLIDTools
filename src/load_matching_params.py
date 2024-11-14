# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:52:06 2024

@author: VASKO
"""

from src.rapidfuzz_token_set_ratio import token2_set_ratio


def load_matching_params(oht_fields):
    print('Loading matching parameters for oht fields:\n', oht_fields)

    # Set fuzzy matching method
    fuzz_method = token2_set_ratio

    # Set text preprocessing differently by field
    fuzz_process = {
        field: True for field in oht_fields
    }
    fuzz_process['Effect level'] = False

    # Set fuzzy matching threshold differently by field
    fuzz_thresholds = {field: 80 for field in oht_fields}
    fuzz_thresholds['Simple Endpoint'] = 101  # !! TODO: check is this right?

    # Set word vector matching threshold differently by field
    vector_fields = [
        'Endpoint',
        'Route of administration',
        'Vehicle',
        'Type of inhalation exposure',
        'Type of inhalation exposure (if applicable)'
    ]
    vector_thresholds = {
        field: 0.40 if field in vector_fields else 0 for field in oht_fields
    }

    return ({
        'fuzz_method': fuzz_method,
        'fuzz_process': fuzz_process,
        'fuzz_thresholds': fuzz_thresholds,
        'vector_thresholds': vector_thresholds
    })