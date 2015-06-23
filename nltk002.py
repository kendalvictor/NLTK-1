import re
import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords

stops = stopwords.words("english")

genre_word0 = [(genre, word)
               for genre in ['news', 'romance']
               for word in brown.words(categories=genre)]

print('')
print('len(genre_word0)             : %d' % len(genre_word0))

genre_word1 = []
news_word1 = []
romance_word1 = []
genre_word_stops1 = []
for genre, word in genre_word0:
    word_lower = word.lower()
    drop = re.search('[^a-z0-9]', word_lower)
    if not drop:
        try:
            stops.index(word_lower)
            genre_word_stops1.append((genre, word_lower))
        except ValueError:
            genre_word1.append((genre, word_lower))
            if genre == 'news':
                news_word1.append(word)
            else:
                romance_word1.append(word)

print('len(genre_word1)             : %d' % len(genre_word1))
print('len(news_word1)              : %d' % len(news_word1))
print('len(romance_word1)           : %d' % len(romance_word1))

set_news = set(news_word1)
set_romance = set(romance_word1)
common = list(set_romance.intersection(set_news))
difference_romance_news = list(set_romance.difference(set_news))
difference_news_romance = list(set_news.difference(set_romance))
print('len(common)                  : %d' % len(common))
print('len(difference_romance_news) : %d' % len(difference_romance_news))
print('len(difference_news_romance) : %d' % len(difference_news_romance))

print('')

cfd = nltk.ConditionalFreqDist(genre_word1)
# print(cfd.conditions())

print('cfd[news].most_common(5)     : %s' % cfd['news'].most_common(5))
print('cfd[romance].most_common(5)  : %s' % cfd['romance'].most_common(5))

common_news_freq = []
news_freq = []
for word, count_news in cfd['news'].items():
    try:
        common.index(word)
    except ValueError:
        news_freq.append((word, count_news))
        continue
    count_romance = cfd['romance'][word]
    common_news_freq.append((word, count_news, count_romance))

common_romance_freq = []
romance_freq = []
for word, count_romance in cfd['romance'].items():
    try:
        common.index(word)
    except ValueError:
        romance_freq.append((word, count_romance))
        continue
    count_news = cfd['news'][word]
    common_romance_freq.append((word, count_news, count_romance))

print('')
print('common_news_freq[0:5]        : %s' % common_news_freq[0:50])
print('news_freq[0:5]               : %s' % news_freq[0:50])
print('')
print('common_romance_freq[0:5]     : %s' % common_romance_freq[0:50])
print('romance_freq[0:5]            : %s' % romance_freq[0:50])
print('')

set_news = set(common_news_freq)
set_romance = set(common_romance_freq)

set_common = set_news.union(set_romance)

# print('len(set_news)                : %d' % len(set_news))
# print('len(set_romance)             : %d' % len(set_romance))
# print('len(set_common)              : %d' % len(set_common))
# print('')

common_news_big = []
common_romance_big = []
common_small = []
big = 2
small = 1
for (word, count_news, count_romance) in common_news_freq:
    if count_news > big*count_romance:
        common_news_big.append((word, count_news, count_romance))
    elif count_romance > big*count_news:
        common_romance_big.append((word, count_news, count_romance))
    elif count_romance == count_news + small or count_romance == count_news - small:
        common_small.append((word, count_news, count_romance))

print('common_news_big[:50]         : %s' % common_news_big[:50])
print('common_romance_big[:50]      : %s' % common_romance_big[:50])
print('common_small[:50]            : %s' % common_small[:50])