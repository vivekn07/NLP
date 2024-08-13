# Import the necessary module from the Natural Language Toolkit (nltk)
import nltk
from nltk.stem import RegexpStemmer

# Create an instance of the RegexpStemmer class with a specific pattern
# The pattern 'ing$|s$|e$|able$' will remove these suffixes if they appear at the end of a word
# The 'min=4' parameter ensures that the stemmed word has at least 4 characters
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)

# Stem the word 'writing' and print the result
print(Reg_stemmer.stem('writing'))