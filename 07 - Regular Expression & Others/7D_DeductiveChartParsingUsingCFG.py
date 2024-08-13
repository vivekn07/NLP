# Install the Natural Language Toolkit (NLTK) library
# pip install nltk

# Import necessary modules from NLTK
import nltk
from nltk import tokenize

# Download the 'punkt' tokenizer models
nltk.download('punkt')

# Define a context-free grammar (CFG)
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  PP -> P NP
  NP -> Det N | Det N PP | 'I'
  VP -> V NP | VP PP
  Det -> 'a' | 'my'
  N -> 'bird' | 'balcony'
  V -> 'saw'
  P -> 'in'
  """)

# Define the sentence to be parsed
sentence = "I saw a bird in my balcony"

# Tokenize the sentence into words
all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)
# Output: ['I', 'saw', 'a', 'bird', 'in', 'my', 'balcony']

# Create a chart parser with the defined grammar
parser = nltk.ChartParser(grammar1)

# Parse the tokenized sentence and print the parse trees
for tree in parser.parse(all_tokens):
  print(tree)
  tree.pretty_print()