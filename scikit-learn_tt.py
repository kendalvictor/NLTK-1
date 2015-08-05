from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB


# 1. Loading the 20 newsgroups dataset

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
# Scikit-learn data set "bunch"
# In tutorial listed as twenty_train data set and I use tt instead
tt = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
names = tt.target_names
len_data = len(tt.data)
len_names = len(tt.filenames)
# Supervised learning algos require a category label for a document.
# Category is the name of the newsgroup.
# For speed/space loaded the target attribute as an array of integers
i = tt.target[:10]
for t in tt.target[:10]:
    name = tt.target_names[t]
    print(name)
print(len(tt.data))
data = tt.data
a = data[6]
print(a)

stop = 1

# 2. Extracting features from text files


# 2.1 Bag of words model
# To perform machine learning first turn content into numerical feature vectors: bags of words
# Assign integer to each word occurring in a document
# For each document i and word j store the count of occurrences in X[i, j]
# There are typically n_features >= 100,000 (distinct words) in the corpus
# Most X[i, j] = zero and high-dimensional sparse datasets: only store non-zero parts of feature vector in memory
# The scipy.sparse matrices are data structures that do exactly this


# 2.2 Tokenizing text
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(tt.data)
s = X_train_counts.shape
count = count_vect.vocabulary_.get(u'algorithm')


# 2.3 From occurrences to frequencies
# Count is good start but longer documents have higher average counts even though they might talk about same topics
# Avoid issues and divide number counts of word in document by total number of words in document: Term Frequencies (tf)
# Another refinement is to downscale weights for words that occur in many documents in the corpus: less informative
# Called Term Frequency times Inverse Document Frequency (tf–idf)
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
s_tf = X_train_tf.shape

# In the above example-code, we fit() method to fit our estimator to the data
# And secondly transform() method to transform our count-matrix to a tf-idf representation
# These two steps can be combined to achieve the same end result:
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
s_tfidf = X_train_tfidf.shape


# 2.4 Training a classifier
# Train classifier to predict category of post and start with naïve Bayes classifier: multinomial variant
clf = MultinomialNB().fit(X_train_tfidf, tt.target)

# Predict outcome on new document need to extract the features using same feature extracting chain as before
# The difference is we call transform instead of fit_transform since they have already been fit to the training set
docs_new = ['God is love', 'OpenGL on the GPU is fast']
X_new_counts = count_vect.transform(docs_new)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

for doc, category in zip(docs_new, predicted):
    print('%r => %s' % (doc, tt.target_names[category]))


stop = 1