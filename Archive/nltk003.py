import nltk, re, pprint
from nltk import word_tokenize

from urllib import request

url = "http://www.latimes.com/nation/la-na-same-sex-marriage-poll-20150609-story.html"

response = request.urlopen(url)

raw = response.read().decode('utf8')

print(type(raw))

print(raw)
