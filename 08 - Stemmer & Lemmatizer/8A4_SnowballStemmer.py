# Import the necessary module from the Natural Language Toolkit (nltk)
import nltk
from nltk.stem import SnowballStemmer

# Create an instance of the SnowballStemmer class for the English language
english_stemmer = SnowballStemmer('english')

# Stem the word 'writing' and print the result
print(english_stemmer.stem('writing'))
