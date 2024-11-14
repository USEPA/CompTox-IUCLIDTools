# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:44:13 2023

@author: VASKO
"""

import regex as re

class custom_tokenizer():
    def __init__(self,
                 base_tokenizer,
                 stopwords,
                 punctuation=['(', ')', ':', '.', ',', '?']
                 ):
        self.tokenizer = base_tokenizer
        self.stopwords = stopwords
        self.punctuation = punctuation

    def prune_stopwords(self, min_len=2):
        self.stopwords = [s for s in self.stopwords if len(s) >= min_len]

    def all_punct(self, text):
        punct = re.findall(f'[{"".join(self.punctuation)}]', text)
        return(''.join(punct) == text)

    def tokenize(self, text):
        tokens = self.tokenizer(text)
        tokens = [t for t in tokens if not t in self.stopwords]
        tokens = [t for t in tokens if not self.all_punct(t)]
        tokens = [t.lower() for t in tokens]
        return(tokens)