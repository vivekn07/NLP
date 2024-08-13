import nltk

# Download the 'treebank' dataset
nltk.download('treebank')

# Import the treebank_chunk module from nltk.corpus
from nltk.corpus import treebank_chunk

# Get the first tagged sentence from the treebank dataset
tagged_sentence = treebank_chunk.tagged_sents()[0]

# Get the first chunked sentence from the treebank dataset
chunked_sentence = treebank_chunk.chunked_sents()[0]

# Draw the chunked sentence
chunked_sentence.draw()
