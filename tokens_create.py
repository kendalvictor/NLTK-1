import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
import re

stop_words = stopwords.words('english')
stop_words = set(stop_words)

#Pickling in
pkl_articles_dict = open('pickles/samuel_dubose/articles.pkl', 'rb')
articles = pickle.load(pkl_articles_dict)
pkl_articles_dict.close()

p1 = re.compile(r'\W+?')
p2 = re.compile(r'[0-9]')

# txt = re.sub(r'\W+?', ' ', txt)
# txt = re.sub(r'[0-9]', '', txt)

txt = ''
tokens = []
for key in articles:
    information =  articles[key]
    txt1 = information['body']
    txt1 = txt1.lower()

    txt1 = p1.sub(' ', txt1)
    txt1 = p2.sub('', txt1)

    tokens00 = word_tokenize(txt1)

    if len(tokens00):
        tokens01 = set(tokens00)
        tokens02 = tokens01.difference(stop_words)
        tokens.append([tokens00, tokens01, tokens02])

    txt = txt + txt1 + ' '

tokens10 = word_tokenize(txt)
tokens11 = set(tokens10)
tokens12 = tokens11.difference(stop_words)

#length of tokens; length of set(tokens); length of set(tokens-stopwords)
tokens.insert(0, [tokens10, tokens11, tokens12])

# Pickling out
output = open('pickles/samuel_dubose/tokens.pkl', 'wb')
pickle.dump(tokens, output)
output.close()