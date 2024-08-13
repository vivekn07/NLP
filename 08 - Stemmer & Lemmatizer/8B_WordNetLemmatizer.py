# Importing the WordNetLemmatizer from nltk.stem
from nltk.stem import WordNetLemmatizer

# Creating an instance of WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Printing the header for the output
print("word :\tlemma")

# Lemmatizing the word 'rocks' and printing the result
print("rocks :", lemmatizer.lemmatize("rocks"))

# Lemmatizing the word 'corpora' and printing the result
print("corpora :", lemmatizer.lemmatize("corpora"))

# Lemmatizing the word 'better' with 'a' (adjective) as the part of speech and printing the result
print("better :", lemmatizer.lemmatize("better", pos="a"))