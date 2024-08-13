# Import the WordNet corpus from NLTK
from nltk.corpus import wordnet

# Get the synsets (sets of synonyms) for the word "active"
synsets = wordnet.synsets("active")
print(synsets)

# Get the antonyms for the lemma 'active' in the synset 'active.a.01'
antonyms = wordnet.lemma('active.a.01.active').antonyms()
print("\n", antonyms)