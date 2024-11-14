# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:57:56 2024

@author: VASKO

Borrowed from `def token_set_ratio()` in:
https://github.com/rapidfuzz/RapidFuzz/blob/fdc3fb3eb7af262a91ceeb401c7fd2e7a4f9a644/src/rapidfuzz/fuzz_py.py#L456
"""

## Wrap with `fuzz._rapidfuzz_scorer()`??

from rapidfuzz._common_py import conv_sequences
from rapidfuzz.fuzz_py import (
    _join_splitted_sequence,
    _norm_distance,
    _split_sequence
)
# from rapidfuzz.distance.Indel_py import distance as indel_distance
from rapidfuzz._utils import is_none
from nltk import edit_distance

from math import ceil

from thefuzz.fuzz import _rapidfuzz_scorer


def _token2_set_ratio(s1, s2, processor=None, score_cutoff=None):
    if is_none(s1) or is_none(s2):
        return 0

    if processor is not None:
        s1 = processor(s1)
        s2 = processor(s2)

    if score_cutoff is None:
        score_cutoff = 0

    s1, s2 = conv_sequences(s1, s2)

    _split_s1 = _split_sequence(s1)
    _split_s2 = _split_sequence(s2)
    tokens_a = set(_split_s1)
    tokens_b = set(_split_s2)

    # in FuzzyWuzzy this returns 0. For sake of compatibility return 0 here as well
    # see https://github.com/rapidfuzz/RapidFuzz/issues/110
    if not tokens_a or not tokens_b:
        return 0

    intersect = list(tokens_a.intersection(tokens_b))
    diff_ab = list(tokens_a.difference(tokens_b))
    diff_ba = list(tokens_b.difference(tokens_a))

    ab_len = len(diff_ab)
    ba_len = len(diff_ba)
    # todo is length sum without joining faster?
    sect_len = len(intersect)

    # string length sect+ab <-> sect and sect+ba <-> sect
    sect_ab_len = sect_len + (sect_len != 0) + ab_len
    sect_ba_len = sect_len + (sect_len != 0) + ba_len

    # one sentence is part of the other one
    if intersect and (not diff_ab or not diff_ba):
        if ab_len == 0 or ba_len == 0:
            return (100)
        else:
            return (max(100 / ab_len, 100 / ba_len))  ## !! Modified to punish longer input text
        # return 100

    # diff_ab_joined = _join_splitted_sequence(sorted(diff_ab))
    # diff_ba_joined = _join_splitted_sequence(sorted(diff_ba))

    # ab_len = len(diff_ab_joined)
    # ba_len = len(diff_ba_joined)
    # # todo is length sum without joining faster?
    # sect_len = len(_join_splitted_sequence(intersect))

    # # string length sect+ab <-> sect and sect+ba <-> sect
    # sect_ab_len = sect_len + (sect_len != 0) + ab_len
    # sect_ba_len = sect_len + (sect_len != 0) + ba_len

    result = 0.0
    cutoff_distance = ceil((sect_ab_len + sect_ba_len) * (1 - score_cutoff / 100))
    # dist = indel_distance(diff_ab_joined, diff_ba_joined, score_cutoff=cutoff_distance)
    dist = edit_distance(_split_s1, _split_s2)  ## !! This was the only part I edited to get token-based edit distance

    if dist <= cutoff_distance:
        result = _norm_distance(dist, sect_ab_len + sect_ba_len, score_cutoff)

    # exit early since the other ratios are 0
    if not sect_len:
        return result

    # levenshtein distance sect+ab <-> sect and sect+ba <-> sect
    # since only sect is similar in them the distance can be calculated based on
    # the length difference
    sect_ab_dist = (sect_len != 0) + ab_len
    sect_ab_ratio = _norm_distance(sect_ab_dist, sect_len + sect_ab_len, score_cutoff)

    sect_ba_dist = (sect_len != 0) + ba_len
    sect_ba_ratio = _norm_distance(sect_ba_dist, sect_len + sect_ba_len, score_cutoff)

    return max(result, sect_ab_ratio, sect_ba_ratio)


def token2_set_ratio(s1, s2, full_process=True):
    return _rapidfuzz_scorer(_token2_set_ratio,
                             s1,
                             s2,
                             force_ascii=False,
                             full_process=full_process
                             )
