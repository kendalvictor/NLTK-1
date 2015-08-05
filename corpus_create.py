from os import listdir
from os import walk
import codecs
from utilities import regex
import pickle

path = 'C:/Users/Aaron/Desktop/Samuel Dubose/'

f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.append([dirpath, filenames])
    # break

articles = {}
for path_files in f:
    dir = path_files[0]
    files = path_files[1]
    for file in files:
        path = dir + '/' + file
        print(path)
        f = codecs.open(path, encoding='utf-8', mode='r')
        txt = f.read()
        f.close()
        if len(txt) > 1:
            title = regex('title').findall(txt)[0][1]
            subtitle = regex('subtitle').findall(txt)[0][1]
            author = regex('author').findall(txt)[0][1]
            editor = regex('editor').findall(txt)[0][1]
            source = regex('source').findall(txt)[0][1]
            outlet = regex('outlet').findall(txt)[0][1]
            other = regex('other').findall(txt)[0][1]
            link = regex('link').findall(txt)[0][1]
            date = regex('date').findall(txt)[0][1]
            slug = regex('slug').findall(txt)[0][1]
            body = regex('body').findall(txt)[0][1]

            art_dict = {'title': title, 'subtitle': subtitle, 'author': author, 'editor': editor, 'source': source,
                        'outlet': outlet, 'other': other, 'link': link, 'date': date, 'slug': slug, 'body': body}

            articles.update({file: art_dict})

# Pickling out
output = open('pickles/samuel_dubose/articles.pkl', 'wb')
pickle.dump(articles, output)
output.close()

#Pickling in
pkl_articles_dict = open('pickles/samuel_dubose/articles.pkl', 'rb')
articles2 = pickle.load(pkl_articles_dict)
pkl_articles_dict.close()