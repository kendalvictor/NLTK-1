import pickle
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

stop_words = stopwords.words('english')
stop_words = set(stop_words)

#Pickling in
pkl_articles_dict = open('pickles/samuel_dubose/articles.pkl', 'rb')
articles = pickle.load(pkl_articles_dict)
pkl_articles_dict.close()

txt = ''
tokens = []
for key in articles:
    information =  articles[key]
    txt1 = information['body']
    txt1 = txt1.lower()
    txt = txt + txt1 + ' '

tokens1 = word_tokenize(txt)
set1 = set(tokens1)
list1 = sorted(list(set1))

# character           dec         hex
# single quote:       0096    :   0060
# single quote:       8216    :   2018
# apostrophe quote:   8217    :   2019
# comma:              8218    :   201a
# single quote:       8219    :   201b
# left quote:         8220    :   201c
# right quote:        8221    :   201d

"""
txt = re.sub(r'\'', '', txt) # word_tokenize splits words like can't and so change to cant
txt = re.sub(r'"', '', txt)
txt = re.sub(r'(<section>)|(</section>)', '', txt)
txt = re.sub(r'!|\$|\(|\)|\?|\.|:|;|\[|\]|,|<|>', '', txt)
# txt = re.sub(r'[0-9]', '', txt)
txt = re.sub(r'--|/', ' ', txt)
txt = re.sub(r'\u0060', '', txt)
txt = re.sub(r'\u2018|\u2019', '', txt)
txt = re.sub(r'\u201a', ',', txt)
txt = re.sub(r'\u201c', '', txt)
txt = re.sub(r'(.\u201d)', '', txt)
"""

txt = re.sub('-', ' ', txt)

txt = re.sub('\u0060', '', txt)
txt = re.sub('\u2018', '', txt)
txt = re.sub('\u2019', '', txt)
txt = re.sub('\u201a', ',', txt)
txt = re.sub('\u201c', '', txt)
txt = re.sub('\u201d', '', txt)

txt = re.sub(r'\W+?', ' ', txt)
txt = re.sub(r'[0-9]', '', txt)

tokens2 = word_tokenize(txt)
set2 = set(tokens2)
list2 = sorted(list(set2))

list3 = list(sorted(set1.difference(set2)))

test1 = list3[18]
print(test1)

print()
run_list = list2
for idx, word in enumerate(run_list):
    begin = idx*15
    end = begin + 15
    print(run_list[begin:end])
    if end >= len(run_list):
        break

stop = 1