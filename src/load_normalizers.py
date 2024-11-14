# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:41:24 2024

@author: VASKO
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer

import spacy
from scispacy.linking import EntityLinker
from scispacy.linking_utils import KnowledgeBase
from scispacy.abbreviation import AbbreviationDetector
from scispacy.candidate_generation import CandidateGenerator
from src.custom_tokenizer import Tokenizer


# --- Load "Normalizers" (tokenizer, scispacy NER)


def load_normalizers():
    print('Loading normalizers')

    # -- Set up tokenizer
    tokenizer = Tokenizer(word_tokenize, stopwords.words('english'))
    tokenizer.prune_stopwords(min_len=2)

    # -- Load linker, NLP info
    linker = CandidateGenerator()

    # Need to pip install model's url before using them
    nlp = spacy.load("en_core_sci_md")
    nlp.add_pipe("abbreviation_detector")
    nlp.add_pipe("scispacy_linker",
                 config={
                     "resolve_abbreviations": True,
                     "linker_name": "umls"
                 }
                 )

    linker = nlp.get_pipe("scispacy_linker")
    threshold = 0.90

    # -- Set up Lemmatizer
    nltk.download('wordnet')
    Lemmatizer = WordNetLemmatizer()

    return ({
        'tokenizer': tokenizer,
        'nlp': nlp,
        'Lemmatizer': Lemmatizer
    })

