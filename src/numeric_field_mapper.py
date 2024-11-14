# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:46:26 2024

@author: VASKO
"""

import numpy as np
import pandas as pd
import src.utils as utils
from src.OHTReader import JSONLData, LookupMap

from scipy.spatial import distance


# Function to split data into given number of bins and obtain bin counts
def get_histogram(vals, nbins, scale='log', fixed_bins=None):
    if scale == 'log':
        vals = vals[vals > 0]
        print('Restricting range to values > 0 due to logscale requested')
    if not fixed_bins is None:
        bins = fixed_bins
    else:
        vmin, vmax = vals.min(), vals.max()
        if scale == 'log':
            bins = get_logscale_bins(vmin, vmax, nbins)
        else:
            bins = np.arange(vmin, vmax)
    return (np.histogram(vals, bins=bins))


# Function to split data into bins spaced on a log scale
def get_logscale_bins(vmin, vmax, nbins):
    logmin = np.log10(vmin)
    logmax = np.log10(vmax)
    logstep = logmax / nbins
    logbins = np.arange(logmin, logmax, logstep)
    bins = np.exp(logbins)
    bins[0] = 0
    return (bins)


def map_numeric_fields(input_file,
                       input_numeric_file,
                       oht_data_file,
                       oht_data_map_file,
                       oht_numeric_fields,
                       na_strings=['Not Specified', 'not specified', -999]
                       ):
    # Load data
    data = utils.load_data(input_file)

    # Load picklist file
    numeric_fields = pd.read_excel(input_numeric_file)[0].tolist()

    # Load numeric OHT data from JSONL file
    # -- Load mapping between JSONL codes and information
    Map = LookupMap(oht_data_map_file, )

    # -- Load JSONL Data
    OHT = JSONLData(oht_data_file, Map)
    for field in oht_numeric_fields:
        OHT.pull_data(field)

    # Drop missing strings for each numeric field and store results
    numeric_data = {}
    for n in numeric_fields:
        num_series = data[n][~data[n].isin(na_strings)]
        num_series = num_series.dropna()
        if len(num_series) > 1:
            numeric_data[n] = num_series

    # -- Compare cosine distances between bin counts of numeric OHT and input fields
    numeric_matches = {}
    for oht_field in oht_numeric_fields:

        # Extract OHT data to compare to
        oht_numeric_data = pd.Series(OHT.data[oht_field])

        # Set up fixed bins based on Effect level, get counts
        nbins = 20
        hist_target, hist_bins = get_histogram(oht_numeric_data, nbins)

        # Loop through all numeric fields
        dist_hists = {}
        for n in numeric_data:

            # Drop missing or not specified data
            d = numeric_data[n]

            # Get bin counts for the same bins used for Effect level counts
            hist_d, _ = get_histogram(d, nbins, fixed_bins=hist_bins)

            # Calculate 1 - cosine distance between bin counts
            if all(hist_d == 0):
                dist_hists[n] = 0
            else:
                dist_hists[n] = 1 - distance.cosine(hist_target, hist_d)

        numeric_matches[oht_field] = utils.top_n(pd.Series(dist_hists), 1)

    return (numeric_matches)



