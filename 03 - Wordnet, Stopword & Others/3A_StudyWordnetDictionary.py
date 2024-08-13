import nltk
from nltk.corpus import wordnet

# Download the WordNet data
nltk.download('wordnet')

# Get synsets (sets of synonyms) for the word "sunrise"
print(wordnet.synsets("sunrise"))

# Print the definition and examples for the first synset of "sunrise"
print("My word is Sunrise:- \n", "Definition:", wordnet.synset("sunrise.n.01").definition())
print("Examples:", wordnet.synset("sunrise.n.01").examples())

# Get the lemma for "sunrise" in the first synset
lemma = wordnet.lemma('sunrise.n.01.sunrise')

# Print the antonyms for the lemma "sunrise"
print("\nAntonym of word Sunrise (Noun):", lemma.antonyms())
