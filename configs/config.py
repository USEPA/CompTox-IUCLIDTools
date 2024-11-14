# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 17:59:49 2024

@author: VASKO
"""

config = {

    # --- OHTS
    # Perform new NLP processing on OHT data?
    ## USER UPDATE !!
    'update_ohts': True,

    # Where the OECD Harmonized Templates are stored
    ## USER UPDATE !!
    'oht_docx_path': 'All OHTs Word Files -Nov 2021',

    # OHT picklist fields of interest
    ## USER UPDATE !!
    'oht_picklist_fields': [
        'Dose descriptor',
        'Effect level',
        'Endpoint',
        'Route of administration',
        'Sex',
        'Species',
        'Test organisms (species)',
        'Strain',
        'Type of inhalation exposure',
        'Type of inhalation exposure (if applicable)',
        'Vehicle'
    ],

    # OHT numeric fields of interest
    ## USER UPDATE !!
    'oht_numeric_fields': [
        'Effect level (numeric)',
        'Effect level (lower)',
        'Effect level (upper)'
    ],

    # OHT fields that designate which OHT a record should be mapped to
    'oht_record_fields': [
        'Simplified Endpoint',
        'Route of administration',
        'Species'
    ],

    # OHT fields to look up based on a predetermined number of values present
    'oht_lookup_fields': [
        'Duration',
        'Generation',
        'Effect level (qualifier)'
    ],

    # The picklist options available for the values depend on the picklist options available for the keys
    'oht_dependent_fields': {'Species': 'Strain'},

    # Name of the JSONL file that stores OHT data
    'oht_data_file': 'data/OHT73.jsonl',

    # Name of the file that maps between JSONL codes and information content
    'oht_data_map_file': 'data/IUCLID6_6_all_fields_update01.xlsx',

    # Name of the output file of OHT picklist values
    'oht_picklist_file': 'output/OHT Picklists.xlsx',

    # Name of the output directory to store NLP-processed OHT data
    'oht_pickle_dir': 'output/OHT Info',

    # Perform new NLP processing on input data?
    ## USER UPDATE !!
    'update_input': True,

    # Name of the input data file to map
    ## USER UPDATE !!
    'input_file': 'data/toxval_full_pull_2022_08_18.xlsx',

    # Name of the output file of input picklist values
    'input_picklist_file': 'output/toxval_picklists.xlsx',

    # Name of the output file of input numeric column names
    'input_numeric_file': 'output/toxval_numeric_fields.xlsx',

    # Name of the output directory to store NLP-processed input data
    'input_pickle_dir': 'output/ToxVal Info'
}
