import nltk
from nltk.corpus import wordnet

# Ensure the WordNet data is downloaded
nltk.download('wordnet')

# Get synsets (sets of synonyms) for the word "computer"
print(wordnet.synsets("computer"))

# Get lemma names for the first synset of "computer"
print(wordnet.synset("computer.n.01").lemma_names())

# Print all synsets and their lemma names for "computer"
for e in wordnet.synsets("computer"):
    print(f'{e} --> {e.lemma_names()}')

# Get lemmas for the first synset of "computer"
print(wordnet.synset('computer.n.01').lemmas())

# Get the synset for the lemma "computing_device" in the first synset of "computer"
print(wordnet.lemma('computer.n.01.computing_device').synset())

# Get the name of the lemma "computing_device" in the first synset of "computer"
print(wordnet.lemma('computer.n.01.computing_device').name())

# Print hyponyms (more specific terms) of "computer"
print("\n\nHyponyms of computer:\n")
syn = wordnet.synset('computer.n.01')
print(syn.hyponyms())
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])

# Print hyponyms of "vehicle"
print("\n\nHyponyms of vehicle:\n")
vehicle = wordnet.synset('vehicle.n.01')
print(vehicle.hyponyms())
print([lemma.name() for synset in vehicle.hyponyms() for lemma in synset.lemmas()])

# Print hyponyms of "car"
print("\n\nHyponyms of car:\n")
car = wordnet.synset('car.n.01')
print(car.hyponyms())
print([lemma.name() for synset in car.hyponyms() for lemma in synset.lemmas()])

# Print the lowest common hypernyms (more general terms) between "car" and "vehicle"
print(car.lowest_common_hypernyms(vehicle))

# Print hypernyms of "vehicle"
print("\n\nHypernyms of vehicle:\n")
vehi1 = wordnet.synset('vehicle.n.01')
print(vehi1.hypernyms())
print([lemma.name() for synset in vehi1.hypernyms() for lemma in synset.lemmas()])