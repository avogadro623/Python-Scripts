#!/usr/bin/env python2
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

import nltk
from nltk.corpus import stopwords
#nltk.download() 
#str stopwords
#print(stopwords.words("english"))

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'alice.txt')).read()

import re
# Use regular expressions to do a find-and-replace
letters_only = re.sub("[^a-zA-Z]",           # The pattern to search for
                      " ",                   # The pattern to replace it with
                      text )  # The text to search
#print(letters_only)
lower_case = letters_only.lower()        # Convert to lower case
words = lower_case.split()               # Split into words
# Remove stop words from "words"
words = [w for w in words if not w in stopwords.words("english")]
#print(type(words))

with open('test.txt', 'w') as f:
    for s in words:
        f.write(s + '\n')

text = open(path.join(d, 'test.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")

# take relative word frequencies into account, lower max_font_size
wordcloud = WordCloud(max_font_size=25, relative_scaling=.5).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
#image = wordcloud.to_image()
#image.show()
