# from nltk.corpus import reuters
# from nltk.corpus import brown
# import nltk
from nltk.tokenize import RegexpTokenizer
import os
from nltk.corpus import PlaintextCorpusReader

BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace('\\', '/')

corpus_root = BASE_DIR + '/NLTK/TestCorpus/'

my_corpus = PlaintextCorpusReader(corpus_root, ['testa1.txt', 'testa2.txt', 'testa3.txt', 'testa4.txt',
                                                'testa5.txt', 'testa6.txt'], encoding='latin-1')

print(my_corpus.fileids())

print('')

print(my_corpus.words('testa1.txt')[0:25])

print('')

tokenizer = RegexpTokenizer(r'\w+')
raw = my_corpus.raw().lower()

print(raw[0: 195])


stop = 1




