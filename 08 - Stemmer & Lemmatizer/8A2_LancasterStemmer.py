# Import the necessary module from the Natural Language Toolkit (nltk)
import nltk
from nltk.stem import LancasterStemmer

# Create an instance of the LancasterStemmer class
Lanc_stemmer = LancasterStemmer()

# Stem the word 'writing' and print the result
print(Lanc_stemmer.stem('writing'))