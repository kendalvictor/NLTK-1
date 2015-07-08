import re
import nltk

rw = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rw for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

cv_word_pairs = [(cv, w) for w in rw for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['so'])

p = re.compile(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$')
w = re.findall(p, 'processes')

stop = 1
