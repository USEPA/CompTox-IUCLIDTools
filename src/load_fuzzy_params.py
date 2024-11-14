# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:52:06 2024

@author: VASKO
"""

from rapidfuzz_token_set_ratio import token2_set_ratio


def load_matching_params():
    # Set fuzzy matching method
    fuzz_method = token2_set_ratio

    # set text preprocessing differently for each field
    fuzz_process = {
        field: True for field in
    }
    fuzz_process['Effect level'] = False
    fuzz_threshold = 80