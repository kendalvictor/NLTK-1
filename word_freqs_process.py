import pickle
from nltk import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import interpolate
import pylab

# 2-dimensional array: freq set; freq set-stopwords' freq cross set-stopwords
pkl_word_freqs = open('pickles/samuel_dubose/word_freqs.pkl', 'rb')
word_freqs_pkl = pickle.load(pkl_word_freqs)
pkl_word_freqs.close()

word_freqs = np.array(word_freqs_pkl)
word_freqs_set = word_freqs

z = np.diagonal(word_freqs_set)

z_max = max(z)
z_min = min(z)
z_mean = np.mean(z)
z_median = np.median(z)
z_std = np.std(z)
z_var = np.var(z)

xx, yy = np.mgrid[0:63, 0:63]
zz = word_freqs_set

plt.figure()
plt.xlim(0, 62)
plt.ylim(0, 62)

plt.pcolor(xx, yy, zz)
plt.colorbar()
plt.title("Article Linguistic Diversity")
plt.show()



"""
xx = range(1, n+1)
ax.set_xticks(xx)
ax.set_xticklabels(['1', '2', '3', '4', '5'])
ax.set_xlim(0, 6)
ax.set_xlabel('Article No')

yy = range(1, n+1)
ax.set_yticks(yy)
ax.set_yticklabels(['1', '2', '3', '4', '5'])
ax.set_ylim(0, 6)
ax.set_ylabel('Article No')

ax.set_zticks([0.0, 0.1, 0.2, 0.3, 0.4])
ax.set_zticklabels(['0.0', '0.1', '0.2', '0.3', '0.4'])
ax.set_zlim(0.0, 0.4)
ax.set_zlabel('Diversity')
"""