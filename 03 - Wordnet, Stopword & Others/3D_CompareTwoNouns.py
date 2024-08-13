import nltk
from nltk.corpus import wordnet

# Get synsets for the words 'football' and 'soccer'
syn1 = wordnet.synsets('football')
syn2 = wordnet.synsets('soccer')

# A word may have multiple synsets, so we need to compare each synset of word1 with each synset of word2
for s1 in syn1:
    for s2 in syn2:
        # Print the path similarity between the synsets
        print("Path similarity of:")
        print(s1, '(', s1.pos(), ')', '[', s1.definition(), ']')
        print(s2, '(', s2.pos(), ')', '[', s2.definition(), ']')
        print("   is", s1.path_similarity(s2))
        print()  # Print a newline for better readability