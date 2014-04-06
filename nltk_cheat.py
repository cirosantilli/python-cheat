#!/usr/bin/env python

"""
Natural language processing toolkit.

Homepage: <http://www.nltk.org/>

Source: <https://github.com/nltk/nltk>

Install:

    sudo pip install nltk

To use ceratin functions, you must data files.

All data files can be downloaded with:

    python -m nltk.downloader all

but that takes up 1.8Gb.

Download interactively with a GUI application:

    python -c 'import nltk; nltk.download()'
"""

import nltk

sentence = """At eight o'clock on Thursday morning
Arthur didn't feel very good."""

print "Input:"
print sentence
print

print "#word_tokenize"
tokens = nltk.word_tokenize(sentence)
print str(tokens)
print

tagged = nltk.pos_tag(tokens)
print "#pos_tag"
print tagged
print

print "#entities"
entities = nltk.chunk.ne_chunk(tagged)
print entities
print

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
print
