from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from numpy import pi, sqrt

raw = "Foo's All human rules are more or less idiotic, I suppose. It is best so, no doubt. The way it is now, the asylums " \
      "can hold the sane people, but if we tried to shut up the insane we should run out of building materials." \
      " -- Mark Twain"

tokenizer = RegexpTokenizer(r'\w+')
words  = tokenizer.tokenize(raw)

sw = stopwords.words('english')
print(len(sw))

reduce = [w.lower() for w in words if w.lower() not in sw]
print(reduce)

stop = 1
