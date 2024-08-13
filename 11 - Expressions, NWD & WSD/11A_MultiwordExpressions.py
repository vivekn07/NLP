# Import necessary modules from nltk
from nltk.tokenize import MWETokenizer
from nltk import sent_tokenize, word_tokenize

# Sample text
s = '''Good cake costs Rs.1500/kg in Hong Kong. Please buy me one of them.\n\nThanks.'''

# Initialize the MWETokenizer with multi-word expressions
mwe = MWETokenizer([('New', 'York'), ('Hong', 'Kong')], separator='-')

# Tokenize the text into sentences
for sent in sent_tokenize(s):
    # Tokenize each sentence into words and apply the MWETokenizer
    print(mwe.tokenize(word_tokenize(sent)))
