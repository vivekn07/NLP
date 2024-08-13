import nltk
from nltk import PCFG

# Define a probabilistic context-free grammar (PCFG)
grammar = PCFG.fromstring('''
NP -> NNS [0.5] | JJ NNS [0.3] | NP CC NP [0.2]
NNS -> "men" [0.1] | "women" [0.2] | "children" [0.3] | NNS CC NNS [0.4]
JJ -> "old" [0.4] | "young" [0.6]
CC -> "and" [0.9] | "or" [0.1]
''')

# Print the defined grammar
print(grammar)

# Create a Viterbi parser with the defined grammar
viterbi_parser = nltk.ViterbiParser(grammar)

# Tokenize the input sentence
token = "old men and women".split()

# Parse the tokenized sentence
obj = viterbi_parser.parse(token)

# Print the parsing output
print("Output:")
for x in obj:
    print(x)