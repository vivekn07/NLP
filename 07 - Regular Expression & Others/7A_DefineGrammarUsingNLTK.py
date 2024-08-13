import nltk
from nltk import tokenize

# Define the grammar using a context-free grammar (CFG)
grammar1 = nltk.CFG.fromstring("""
S -> VP
VP -> V NP
NP -> Det N
Det -> 'that'
N -> 'flight'
V -> 'Book'
""")

# Tokenize the sentence
sentence = "Book that flight"
all_tokens = tokenize.word_tokenize(sentence)
print(all_tokens)

# Create a chart parser with the defined grammar
parser = nltk.ChartParser(grammar1)

# Parse the sentence and print the parse trees
for tree in parser.parse(all_tokens):
    print(tree)
    tree.draw()
