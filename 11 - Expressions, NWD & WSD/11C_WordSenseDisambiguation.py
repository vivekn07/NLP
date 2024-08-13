# Word Sense Disambiguation
from nltk.corpus import wordnet as wn


def get_first_sense(word, pos=None):
    # Retrieve the synsets for the word with the specified part of speech (pos)
    if pos:
        synsets = wn.synsets(word, pos)
    else:
        synsets = wn.synsets(word)
    return synsets[0]


# Get the first sense of the word 'bank'
best_synset = get_first_sense('bank')
if best_synset:
    print('%s: %s' % (best_synset.name(), best_synset.definition()))
else:
    print('No synset found for the word "bank"')

# Get the first sense of the word 'set' as a noun
best_synset = get_first_sense('set', 'n')
if best_synset:
    print('%s: %s' % (best_synset.name(), best_synset.definition()))
else:
    print('No synset found for the word "set" as a noun')

# Get the first sense of the word 'set' as a verb
best_synset = get_first_sense('set', 'v')
if best_synset:
    print('%s: %s' % (best_synset.name(), best_synset.definition()))
else:
    print('No synset found for the word "set" as a verb')