import nltk
import numpy

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

from nltk import tokenize
from nltk import tag
from nltk import chunk

# Sample paragraph for processing
para = "Natural language processing (NLP) is a machine learning technology that gives computers the ability to interpret, manipulate, and comprehend human language."

# Sentence tokenization
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n", sents)

# Word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
    words = tokenize.word_tokenize(sents[index])
    print(words)

# POS Tagging
tagged_words = []
for index in range(len(sents)):
    tagged_words.append(tag.pos_tag(tokenize.word_tokenize(sents[index])))
print("\nPOS Tagging\n===========\n", tagged_words)

# Chunking
tree = []
for index in range(len(sents)):
    tree.append(chunk.ne_chunk(tagged_words[index]))

print("\nchunking\n========\n")
print("Tree: ", tree)