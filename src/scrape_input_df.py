# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:18:38 2024

@author: VASKO
"""

import regex as re
import pandas as pd
import pickle


def check_if_numeric_(x, na_strings):
    try:
        float(x)
        return (True)
    except:
        if x in na_strings:
            return (True)
        else:
            return (False)


def check_if_numeric(series, na_strings=['Not Specified']):
    if series.dtype.kind in ('b', 'c', 'f', 'i', 'u', 'm', 'M'):
        return (True)
    else:
        check = series.apply(lambda x: check_if_numeric_(x, na_strings))
        return (check.all())


def check_if_uuid_(x):
    if len(str(x)) == 32:
        match = re.match('[a-fA-F0-9]+', str(x))
        if match:
            return (match.span() == (0, 32))
        else:
            return (False)
    else:
        return (False)


def check_if_uuid(series, na_strings=['Not Specified']):
    series = series[~series.isin(na_strings)]
    check = series.apply(lambda x: check_if_uuid_(x))
    return (check.all())


# Drop fields where more than 90% of values are formatted like URLs
def check_if_url(series, na_strings=['Not Specified'], threshold=0.90):
    series = series[~series.isin(na_strings)]
    check = series.apply(lambda x: check_if_url_(x))
    return (check.mean() > threshold)


def check_if_url_(x):
    url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    # from https://www.tutorialspoint.com/python-program-to-check-for-url-in-a-string
    match = re.match(url, str(x))
    if match:
        return (match.span() == (0, len(x)))
    else:
        return (False)


def check_proportion_unique(series, threshold):
    prop_unique = series.nunique() / len(series.dropna())
    return (prop_unique < threshold)


def check_nchar(series, threshold):
    max_length = series.apply(lambda x: len(str(x))).max()
    return (max_length < threshold)


# Drop fields where more than 90% of values are formatted like DTXSIDs
def check_if_dtxsid(series, threshold=0.90):
    series = series[~series.isna()]
    check = series.apply(lambda x: check_if_dtxsid_(x))
    return (check.mean() > threshold)


def check_if_dtxsid_(x):
    dtxsid = 'dtxsid\d{7,9}'
    match = re.match(dtxsid, str(x).lower())
    if match:
        return (match.span() == (0, len(x)))
    else:
        return (False)


def separate_field_types(data, unique_threshold, nchar_threshold):
    picklist_fields = []
    numeric_fields = []
    for d in data:
        if check_if_numeric(data[d]):
            numeric_fields.append(d)
        else:
            if not check_if_uuid(data[d]):
                if not check_if_dtxsid(data[d]):
                    if not check_if_url(data[d]):
                        if check_nchar(data[d], nchar_threshold) and \
                                check_proportion_unique(data[d], unique_threshold):
                            picklist_fields.append(d)
    return (picklist_fields, numeric_fields)


def _drop_text(string, drop):
    if drop:
        string = str(string)
        string = string.lower().replace(drop.lower(), '')
    return (string)


def drop_text(opts, drop):
    if len(opts.shape) == 1:
        opts = opts.apply(_drop_text, drop=drop)
    elif len(opts.shape) > 1:
        for opt in opts:
            opts[opt] = opts[opt].apply(_drop_text, drop=drop)
    return (opts)


def clean_input_opts(opts, drop='other'):
    opts = opts.reset_index(drop=True)

    # Drop strings in text that are not helpful to mapping
    opts = drop_text(opts, drop)

    # Push to lowercase
    if isinstance(opts, pd.Series):
        opts = opts.str.lower()
    else:
        opts = opts.apply(lambda x: x.str.lower())

    # Format for next step
    opts = opts.dropna(how='all')
    opts = opts[opts != '']

    # Get counts for optisons
    opts = opts.value_counts().reset_index()

    return (opts)


def scrape_input_df(user_df, input_picklist_file, input_numeric_file):
    # # read in data, save off as pickle file for easier reload
    # print('Reading in data file:\n', input_file)
    # data = pd.read_excel(input_file)
    #
    # print('Saving to pickle file:\n', input_file.replace('.xlsx', 'pkl'))
    # with open(input_file.replace('.xlsx', '.pkl'), 'wb') as fp:
    #     pickle.dump(data, fp)

    # for quicker debugging:
    # with open(input_file.replace('.xlsx', '.pkl'), 'rb') as fp:
    #    data = pickle.load(fp)

    # determine which input fields are plausible numeric vs. picklist fields
    print('Selecting possible picklist fields.')
    picklist_fields, numeric_fields = separate_field_types(
        user_df,
        unique_threshold=1,
        nchar_threshold=500
    )

    # loop through possible picklist fields and pull unique picklist options
    picklist_df = pd.DataFrame()
    for field in picklist_fields:
        tmp = clean_input_opts(user_df[field])
        tmp.columns = ['Options', 'count']
        tmp.insert(0, 'Field', field)

        picklist_df = pd.concat([
            picklist_df,
            tmp
        ])

    # export picklist options to dataframe
    picklist_df.to_excel(input_picklist_file, index=False)

    # export possible picklist fields
    picklist_outname = input_picklist_file.replace('.xlsx', '_fieldnames.xlsx')
    pd.Series(picklist_fields).to_excel(picklist_outname, index=False)

    # export possible numeric fields
    pd.Series(numeric_fields).to_excel(input_numeric_file, index=False)

## TODO: accommodate counts in code