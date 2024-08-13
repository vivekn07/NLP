# pip install spacy
# python -m spacy download en_core_web_sm
# python -m spacy download en

import spacy
import nltk
from nltk.tokenize import word_tokenize

# Load the spaCy model
sp = spacy.load('en_core_web_sm')

# Add the word 'play' to the spaCy stop word collection
all_stopwords = sp.Defaults.stop_words
all_stopwords.add("play")

# Sample text
text = "Viveksingh likes to play cricket, however he is not too fond of basketball."

# Tokenize the text using NLTK
text_tokens = word_tokenize(text)

# Remove stopwords from the tokenized text
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

# Remove 'not' from the stop word collection
all_stopwords.remove('not')

# Remove stopwords with the updated list
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
