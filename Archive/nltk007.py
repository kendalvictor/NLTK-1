import nltk
from nltk.corpus import gutenberg, nps_chat
from nltk.corpus import wordnet
import re

"""
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
x = fdist.most_common(5)
y = [char for (char, count) in fdist.most_common()]
n = len(y)
s = 'Monty Python'
print(s[1:5])

word_list = [w for w in nltk.corpus.words.words('en') if w.islower()]
z = [w for w in word_list if re.search('ed$', w)]

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = sum(1 for n in integers if n > 5)
m = sum(integers)
p = sum(n for n in integers if n > 5)

s = '2009-12-31'
p = re.compile(r'^[0-9]{4}|[0-9]{2}|[0-9]{2}$')
f = re.findall(p, s)
i = [int(c) for c in f]

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
m = moby.findall(r'<a> (<.*>) <man>')
print(m)
"""

s = 'now is the time for some serious marketing'
p = re.compile(r's')
ss = re.findall(p, s)
sss = nltk.re_show(r's', s)

stop = 1


