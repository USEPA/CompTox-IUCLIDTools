# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:45:20 2023

@author: VASKO
"""

import pandas as pd
import numpy as np
import regex as re
import seaborn as sns
import pickle
import copy
from thefuzz import fuzz
from scipy.spatial import distance
import matplotlib.pyplot as plt
from sklearn import preprocessing
from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from thefuzz import utils as futils
from rapidfuzz.fuzz_py import (
    _join_splitted_sequence,
    _split_sequence
)


# load data from pickle file
def load_data(input_file):
    with open(input_file.replace('.xlsx', '.pkl'), 'rb') as fp:
        data = pickle.load(fp)
    return (data)


# load optInfo class from pickle file
def load_optInfo(indir, field):
    field_name = field.replace(':', '')
    with open(f'{indir}/{field_name} Info.pkl', 'rb') as fp:
        optInfo = pickle.load(fp)
    return (optInfo)


def get_match_values(x):
    return (x[0][0] if len(x[0]) > 0 else '')


def get_match_scores(x):
    score = float('nan')
    if x[1] == 'exact match':
        score = 100
    elif x[1]:
        score = x[2][0]
    return (score)


# store data related to picklist options in a dictionary, keyed by the options
def store_opt_info(opts, info):
    return ({
        opt: i for opt, i in zip(opts, info)
    })


# tokenize picklist options and get counts of each token
def get_token_counts(value_counts, tokenizer, lemmatizer=None):
    tokens = {}
    for term, count in value_counts.items():
        if isinstance(term, str):
            term = map_sex(term)  # Put this here??
            doc = tokenizer.tokenize(term)
            for token in doc:
                if lemmatizer:
                    token = get_lemma(token, lemmatizer, full_process=True)
                if token in tokens:
                    tokens[token] += count
                else:
                    tokens[token] = count
    df = pd.Series(tokens).reset_index(drop=False)
    return (df)


# map isolated "m" and "f" strings to "male" and "female"
def map_sex(text):  # Move this outside of tokenizer so only get remapped if whole field is M/F??
    if text.lower() == 'm':
        return ('male')
    elif text.lower() == 'f':
        return ('female')
    elif text.lower() == 'm/f':
        return ('male/female')
    else:
        return (text)


def find_sex_column(data, n_matches=1):
    match_pattern = 'male|(?:m|f|m/f)$'
    return (find_match_column(data, match_pattern, n_matches))


def find_duration_column(
        data,
        n_matches=1,
        # time_units = ['h', 'hours', 'd', 'days', 'weeks', 'wk', 'months'],
        time_units=['hours', 'days', 'weeks', 'wk', 'months'],
        other_patterns=['GD', 'LD', 'PND']
):
    time_units += [' ' + unit for unit in time_units]
    # time_patterns = ['[0-9]' + unit for unit in time_units]
    time_patterns = time_units + other_patterns
    match_pattern = '|'.join(time_patterns)
    return (find_match_column(data, match_pattern, n_matches))


def find_generation_column(data, n_matches=1):
    generations = ['P0', 'P1', 'F1', 'F2', 'F3']
    match_pattern = '|'.join(generations)
    match_pattern = f'(?:{match_pattern})$'
    return (find_match_column(data, match_pattern, n_matches))


def find_qualifier_column(data, n_matches=1):
    qualifiers = ['<', '<=', '>', '>=']
    match_pattern = '|'.join(qualifiers)
    return (find_match_column(data, match_pattern, n_matches))


def find_units_column(data, n_matches=1):
    units = [
        'bw', 'diet', 'ppm', 'drinking water', 'air'
        #    'ng/mg', 'µg/mg', 'ug/mg', 'mg/kg', 'g/kg',
        #    'cells/kg', 'CFU/kg', 'ITU/kg', 'IU/kg', 'OB/kg',
        #    'cells/g', 'CFU/g', 'ITU/g', 'IU/g', 'OB/g',
        #    'ng/L', 'µg/L', 'ug/L', 'mg/L', 'g/L',
        #    'cells/L', 'CFU/L', 'ITU/L', 'IU/L', 'OB/L',
        #    'mg/kg', 'mg/L'
    ]
    match_pattern = '|'.join(units)
    return (find_match_column(data, match_pattern, n_matches))


def find_match_column(data, match_pattern, n_matches=1, threshold=0.1):
    match_counts = data.apply(
        lambda x: count_with_string(x, f"(?i){match_pattern}"),
        axis=0
    )
    match_counts = match_counts.sort_values(ascending=False)
    if match_counts[0] > threshold:
        match_counts = match_counts[match_counts > threshold]
        return (match_counts.index[0:n_matches].tolist())


def find_column_by_name(match_column, columns, threshold=50):
    score_df = pd.DataFrame({
        'scores': [fuzz.token_set_ratio(match_column, c) for c in columns],
        'columns': columns
    })
    score_df = score_df[score_df['scores'] < 100]
    score_df = score_df[score_df['scores'] >= threshold]
    return (score_df['columns'].tolist())


def count_values(series, na_strings=['Not Specified', 'not specified']):
    series = pd.Series(series)
    series = series[~series.isin(na_strings)]
    return (series.value_counts())


def count_with_string(series, string):
    counts = count_values(series)
    if len(counts) > 0:
        counts.index = counts.index.astype(str)
        idx = counts.index.str.contains(string)
        return (counts[idx].sum() / counts.sum())
    else:
        return (0)


def calc_proportion(df_overlap, df_original):
    num = len(df_overlap)
    den = len(df_original)
    if den != 0:
        return (num / den)  # normalize by fraction of OHT data that matched
    else:
        return (float('nan'))


def calc_scale(df_overlap1, df_original1, df_overlap2=None, df_original2=None):
    prop1 = calc_proportion(df_overlap1, df_original1)
    if not df_overlap2 is None and not df_original2 is None:
        prop2 = calc_proportion(df_overlap2, df_original2)
    else:
        prop2 = 0
    return (max(prop1, prop2))


# calculate and scale the dot product between frequency distribution counts
#  (use as a measure of similarity)
def calc_similarity(counts1, counts2, scale):
    if len(counts1) > 0:
        z1 = preprocessing.normalize([counts1])[0]
        z2 = preprocessing.normalize([counts2])[0]
        dot = np.dot(z1, z2)
        return (dot * scale)
    else:
        return (0)


# return all indices in x with scores greater than a specified threshold
def id_pass(x, threshold=0.9):
    x = x.sort_values()
    max_idx = x.index[x > threshold]
    return (max_idx.tolist())


# return all indices in x with scores that match the maximum score
def id_max(x):
    max_val = x.max()
    if max_val > 0:
        max_idx = x.index[x == max_val]
        return (max_idx.tolist())


# return the indices in x with the top n highest scores
def top_n(x, n=3, return_score=False):
    x = x[x > 0]
    x = x.sort_values(ascending=False)
    if return_score:
        return ([round(n, 2) for n in x[0:n]])
    else:
        return (x.index[0:n].tolist())


## -- for picklist mapping

def format_option(option, punctuation=['(', ')', ':', '.', ',', '?', ' ']):
    while option[0:2] == '- ':
        option = option[2:]
    if len(option) > 0:
        while option[-1] in punctuation:
            option = option[0:-1]
    return (option)


def remove_brackets(string):
    string = re.sub("\(.*?\)", "", string)
    string = re.sub("\[.*?\]", "", string)
    string = format_option(string)
    return (string)


def get_pre_punctuation(string, punctuation=['[', '(', ':', '.']):
    locs = []
    for p in punctuation:
        loc = string.find(p)
        if loc > -1:
            locs.append(loc)
    if len(locs) > 0:
        min_loc = min(locs)
        if min_loc > -1:
            string = format_option(string[0:min_loc])
    return (string)


# tokenize and clean string, then proces with nlp to extract word vector
def get_vector(string, nlp):
    tokens = word_tokenize(string)
    tokens = [t.strip(punctuation) for t in tokens]
    tokens = [t for t in tokens if not t.isnumeric()]
    tokens = [t for t in tokens if t != '']
    doc = nlp(' '.join(tokens))
    return (doc.vector)


# process string with nlp and extract cui information
def get_cui(string, nlp, cui_threshold=0.8):
    doc = nlp(string)
    cuis = []
    for e in doc.ents:
        if len(e._.kb_ents) > 0:
            cui, cui_score = e._.kb_ents[0]
            if cui_score > cui_threshold: cuis.append(cui)
    cuis.sort()
    return (' '.join(cuis))


# lemmatize the input string, optionally cleaning as speficied by `full_process`
def get_lemma(string, Lemmatizer, full_process):
    if full_process:
        string = futils.full_process(string, force_ascii=True)
    split_string = _split_sequence(string)
    lemma_list = [Lemmatizer.lemmatize(s) for s in split_string]
    return (_join_splitted_sequence(lemma_list))


# calculate the cosine distance between two (word) vectors
def get_distance(v1, v2):
    if not (v1 == 0).all() and not (v2 == 0).all():
        return (distance.cosine(v1, v2))
    else:
        return (float('nan'))


# sort the matching scores that are above `threshold`, according to direction specified by `op`
def sort_scores(scores, threshold, op):
    scores = scores.dropna()
    if op == '<':
        scores = scores[scores < threshold]
        scores = scores.sort_values()
    elif op == '>':
        scores = scores[scores > threshold]
        scores = scores.sort_values(ascending=False)
    elif op == '=':
        scores = scores[scores == threshold]
    else:
        print('equality operator not recognized')

    if len(scores) > 0:
        score = scores.values.tolist()
        match = scores.index.tolist()
    else:
        score = float('nan')
        match = []
    return (match, score)


# Get strain dictionary (assumes species is in brackets following ' - ')
def split_text_options(string):
    try:
        value_text, key_text = string.split(' - ')
        key_text = re.findall('\[(.*?)\]', key_text)[0]
        return (key_text, value_text)
    except ValueError:
        return (None, None)


def get_by_index(values, index):
    return (pd.Series(values)[index].reset_index(drop=True))


# filter picklist according to affiliated oht and field
def filter_picklist(picklist, oht, field):
    return (
        picklist[
            (picklist['OHT'] == str(oht)) & (picklist['Field'] == field)
            ]['Options']
    )


# filter optInfo attributes according to whether the tokens are in a list
def filter_info(optInfo, options):
    idx = optInfo.opts.isin(options).reset_index().index.tolist()
    optInfo.opts = optInfo.opts.iloc[idx]
    optInfo.cuis = filter_optlist(optInfo.cuis, idx)
    optInfo.word_vectors = filter_optlist(optInfo.word_vectors, idx)
    optInfo.lemmas = filter_optlist(optInfo.lemmas, idx)
    return (optInfo)


# filter a list by an index
def filter_optlist(optlist, idx):
    return ([o for i, o in enumerate(optlist) if i in idx])


def prep_input_opts(opts,
                    drop='other',
                    counts=False,
                    abbreviations_list=[]
                    ):
    # Set up input columns to index
    opts_columns = opts.columns.tolist()

    # Handle counting, if required
    if counts:
        opts = opts.groupby(
            opts_columns
        ).value_counts().reset_index()
    else:
        opts = opts.drop_duplicates()

    # Handle abbreviation definitions, if required
    for field, abbrev_defs in zip(opts_columns, abbreviations_list):
        if abbrev_defs:
            opts[field] = opts[field].apply(
                lambda x: define_abbreviations(x, abbrev_defs)
            )

    return (opts)


def clean_oht_opts(series_opts, abbreviation_definitions=None):
    series_opts = series_opts.str.lower()
    series_opts = series_opts.drop_duplicates()

    if abbreviation_definitions:
        series_opts = series_opts.apply(
            lambda x: define_abbreviations(x, abbreviation_definitions)
        )
    return (series_opts)


# wrapper for `define_abbreviation_` function
def define_abbreviations(string, abbreviation_dict):
    for abbreviation, definition in abbreviation_dict.items():
        string = define_abbreviation_(string, abbreviation, definition)
    return (string)


# replace an abbreviation with its given definition
def define_abbreviation_(string, abbreviation, definition):
    return (string.lower().replace(abbreviation.lower(), definition.lower()))


# get indices of dependent options
def get_dependent_index(oht_opts, dependent_opts):
    oht_opts = oht_opts.reset_index(drop=True)
    oht_opts = oht_opts.apply(lambda x: split_text_options(x)[1])
    return (oht_opts[oht_opts.isin(dependent_opts)].index)


# get matches for picklist options based on info from target string and a second
#   string on which the target options depend
def get_dual_match(input_pair,
                   match1,
                   dependent_input,
                   input_dict2,
                   ohtInfo2,
                   dependent_dict,
                   num_opts_suggested=3,
                   fuzz_threshold=80,
                   vector_threshold=0.4,
                   cui_threshold=20,
                   cui_ent_threshold=0.75,
                   fuzz_func=fuzz.partial_ratio
                   ):
    if match1[1][0]:
        map1 = match1[0][0]
    else:
        map1 = None

    # Map input options for secondary field
    if map1 in dependent_dict:
        oht_index = get_dependent_index(
            ohtInfo2.opts,
            dependent_dict[map1]
        )
        ohtInfo2.opts = pd.Series(dependent_dict[map1])
        ohtInfo2.cuis = get_by_index(ohtInfo2.cuis, oht_index)
        ohtInfo2.lemmas = get_by_index(ohtInfo2.lemmas, oht_index)
        ohtInfo2.word_vectors = filter_optlist(ohtInfo2.word_vectors, oht_index)

        match2 = get_single_match(
            input_pair[dependent_input],
            input_dict2,
            ohtInfo2,
            vector_threshold=vector_threshold,
            fuzz_threshold=fuzz_threshold,
            fuzz_func=fuzz_func,
            cui_threshold=cui_threshold,
            cui_ent_threshold=cui_ent_threshold
        )

    else:
        match2 = get_single_match(
            input_pair[dependent_input],
            input_dict2,
            ohtInfo2,
            vector_threshold=vector_threshold,
            fuzz_threshold=fuzz_threshold,
            fuzz_func=fuzz_func,
            cui_threshold=cui_threshold,
            cui_ent_threshold=cui_ent_threshold
        )

    # Output results as DataFrame
    match2 = (
        match2[0][0:num_opts_suggested],
        match2[1][0:num_opts_suggested],
        match2[2][0:num_opts_suggested]
    )

    return (match2)


# get matches for picklist options based on single string information
def get_single_match(token,
                     toxinfo,
                     ohtInfo,
                     fuzz_threshold=80,
                     vector_threshold=0.4,
                     cui_threshold=20,
                     cui_ent_threshold=0.75,
                     fuzz_func=fuzz.partial_ratio
                     ):
    match = []
    method = None
    score = float('nan')

    # Check for exact match
    match, score, method = get_exact_match(token, ohtInfo)

    # Try NLP-based matching: lemmas
    if method is None:
        match, score, method = get_lemma_match(
            toxinfo['lemmas'][token],
            ohtInfo,
            fuzz_func,
            fuzz_threshold
        )

    # Try NLP-based matching: UMLS-concepts
    if method is None:
        match, score, method = get_cui_match(
            toxinfo['cuis'][token],
            ohtInfo,
            cui_ent_threshold,
            fuzz_func,
            fuzz_threshold
        )

        if method is None:
            match, score, method = get_vector_match(
                toxinfo['word_vectors'][token],
                ohtInfo,
                vector_threshold
            )

    return (match, method, score)


# function to log the name of the matching method, if a match was successful
def name_method(match, method_name):
    if len(match) > 0:
        return (method_name)
    else:
        return (None)


# compare input/oht strings to determine if they match exactly
def get_exact_match(string, ohtInfo):
    match = [o for o in ohtInfo.opts if string == o]
    method = name_method(match, 'exact match')
    return (match, [100], [method])


# execute the desired method of fuzzy matching over the input/oht strings
def get_fuzzy_match(string, oht_compare, oht_opts, fuzz_func, fuzz_threshold):
    fuzzy_scores = pd.Series(
        [fuzz_func(string, o) for o in oht_compare],
        index=oht_opts
    )
    match, score = sort_scores(fuzzy_scores, fuzz_threshold, '>')
    method = name_method(match, 'fuzzy match')
    return (match, score, method)


# get potential picklist option matches based on fuzzy matching with lemmas
def get_lemma_match(target_lemma, ohtInfo, fuzz_func, fuzz_threshold):
    match, score, _ = get_fuzzy_match(
        target_lemma,
        ohtInfo.lemmas,
        ohtInfo.opts,
        fuzz_func,
        fuzz_threshold
    )
    method = name_method(match, 'lemma fuzzy match')
    return (match, score, method)


# get potential picklist option matches based on fuzzy matching with cuis
def get_cui_match(target_cui, ohtInfo, cui_ent_threshold, fuzz_func, fuzz_threshold):
    match, score = [], float('nan')
    if len(target_cui) > 0:
        match, score, _ = get_fuzzy_match(
            target_cui,
            ohtInfo.cuis,
            ohtInfo.opts,
            fuzz_func,
            fuzz_threshold
        )
    method = name_method(match, 'cui match')
    return (match, score, method)


# get potential picklist option matches based on word vector distances
def get_vector_match(target, ohtInfo, vector_threshold):
    match, score = [], float('nan')
    if not (target == 0).all():
        distances = ohtInfo.word_vectors.apply(
            lambda x: get_distance(x, target)
        )
        match, score = sort_scores(distances, vector_threshold, '<')
    method = name_method(match, 'word vector match')
    return (match, score, method)


# get the proportion of total values matched, including input duplicates
def get_prop_matched(values, count_dict):
    values = values.drop_duplicates()
    total = sum(count_dict.values())
    match_count = sum([count_dict[v] for v in values if v in count_dict])
    return (
        pd.Series({
            True: match_count / total,
            False: 1 - match_count / total
        })
    )


# Class to store token, cui, lemma, and word vector information for picklist options
class optInfo():
    def __init__(self, opts, counts=None):
        self.opts = opts
        if not counts is None: self.counts = counts.tolist()

    def get_cuis(self, nlp, cui_ent_threshold):
        self.cui_ent_threshold = cui_ent_threshold
        self.cuis = [
            get_cui(o, nlp, cui_ent_threshold) for o in self.opts
        ]

    def get_lemmas(self, Lemmatizer, fuzz_process):
        self.lemmas = [
            get_lemma(o, Lemmatizer, fuzz_process) for o in self.opts
        ]

    def get_vectors(self, nlp):
        self.word_vectors = pd.Series(self.opts).apply(
            lambda x: get_vector(x, nlp)
        )
        self.word_vectors.index = self.opts