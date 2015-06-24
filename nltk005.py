import nltk
from nltk.corpus import gutenberg
from nltk.corpus import wordnet
import re

"""
print(ord('e'))
print(hex(101))
print(int(0x0065))
a = 'hello world'
p = re.compile(r'\u0065')
f = re.findall(p, a)
print(f)
"""

"""
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x = [i for sub_list in nested_list for i in sub_list]

y = []
for sub_list in nested_list:
    [y.append(i) for i in sub_list]
"""

"""
j = 'This is a rather uninteresting sentence about my positive attitude'
j = j.lower()
p = re.compile(r'^[aeiou]+|[aeiou]+$|[^aeiou]')
f = re.findall(p, j)
f = ''.join(f)
"""

"""
rw = nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rw for cv in re.findall(r'[ptksvr][aeiou]', w)]
cfd = nltk.ConditionalFreqDist(cvs)
cfd.tabulate()

cv_word_pairs = [(cv, w) for w in rw for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index['so'])
"""


p = re.compile(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$')
w = re.findall(p, 'processes')

stop = 1

