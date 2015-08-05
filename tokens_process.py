import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt

#tokens; set(tokens); set(tokens-stopwords)
pkl_tokens = open('pickles/samuel_dubose/tokens.pkl', 'rb')
tokens_pkl = pickle.load(pkl_tokens)
pkl_tokens.close()

diversity = []
list_tokens = tokens_pkl[1:]

word_freqs0 = []
for idx0, tokens0 in enumerate(list_tokens):
    ssw0 = tokens0[2]
    word_freqs1 = []
    for idx1, tokens1 in enumerate(list_tokens):
        ssw1 = tokens1[2]
        nt1 = len(tokens1[0])
        ns1 = len(tokens1[1])
        nssw1 = len(tokens1[2])
        ncross10 = len(ssw1.intersection(ssw0))
        word_freqs1.append(ncross10/nt1)
    word_freqs0.append(word_freqs1)

# 2-dimensional array: freq set; freq set-stopwords' freq cross set-stopwords
output = open('pickles/samuel_dubose/word_freqs.pkl', 'wb')
pickle.dump(word_freqs0, output)
output.close()