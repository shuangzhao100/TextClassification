#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:15:31 2022

@author: aylin
"""

# First install gensim in the same python environment you will run this notebook from
# Usually pip install gensim, but YMMV

from gensim.models import word2vec
from gensim.models import KeyedVectors

# First download the text8 corpus: http://mattmahoney.net/dc/text8.zip
# unzip in the same directory from which you will run this notebook
# (This corpus is not typical text.)
sentences = word2vec.Text8Corpus('text8')

# Train the model. (This step can take a minute or more.  Nothing will happen for a while.)
#model = word2vec.Word2Vec(sentences, vector_size=100, window=5, min_count=5, workers=4)
# min_count is the frequency threshold
# window size depends, need to experiment

# save the model to a file, to avoid retraining (although with Jupyter notebooks this is less of an issue)
#model.save('text.model')

# now load the model from the file
model = word2vec.Word2Vec.load('text.model')

# Now we can use the model to infer things about words

# Ex: Find the top ten terms that are closest to man
print(model.wv.most_similar(['woman'], topn=3))
# be aware of the case sensitivity, make all training set lower case


# Ex: Find the term that is close to woman and king, but far from man.
# Return the top 1 best match. (Can you guess what it will be?)
print(model.wv.most_similar(positive=['woman', 'king'], negative=['man'], topn=1))

# Ex: Now return the top 2 best matches.  Can you guess what the second most similar term will be?
print(model.wv.most_similar(positive=['woman', 'doctor'], negative=['man'], topn=1))


print('\ncastle top 3')
print(model.wv.most_similar(['programming'], topn=3))
