from nltk.tag import UnigramTagger
from nltk.corpus import treebank

# Get the first 10 tagged sentences from the Treebank corpus for training
train_sents = treebank.tagged_sents()[:10]

# Initialize the UnigramTagger with the training sentences
tagger = UnigramTagger(train_sents)

# Print the first sentence from the Treebank corpus
print(treebank.sents()[0])

# Tag the first sentence using the UnigramTagger and print the result
print('\n', tagger.tag(treebank.sents()[0]))

# Tag the first sentence again (this line is redundant and can be removed)
tagger.tag(treebank.sents()[0])

# Override the context model with a custom model
tagger = UnigramTagger(model={'Pierre': 'NN'})

# Tag the first sentence using the updated UnigramTagger and print the result
print('\n', tagger.tag(treebank.sents()[0]))
