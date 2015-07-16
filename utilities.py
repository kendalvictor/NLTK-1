import re
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize

def get_text(file):
    """Read text from a file, normalizing whitespace and stripping HTML markup."""
    text = open(file).read()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub('\s+', ' ', text)
    return text