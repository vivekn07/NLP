# Import the necessary module from the Natural Language Toolkit (nltk)
import nltk
from nltk.stem import PorterStemmer

# Create an instance of the PorterStemmer class
word_stemmer = PorterStemmer()

# Stem the word 'writing' and print the result
print(word_stemmer.stem('writing'))
