import nltk
from nltk.tag import DefaultTagger
from nltk.corpus import treebank

# Download the treebank corpus
nltk.download('treebank')

# Creating a DefaultTagger that tags every word as 'NN' (noun)
exptagger = DefaultTagger('NN')

# Getting tagged sentences from the treebank corpus starting from the 1000th sentence
testsentences = treebank.tagged_sents()[1000:]

# Evaluating the tagger on the test sentences and printing the accuracy
print(exptagger.evaluate(testsentences))

# Tagging a list of sentences
# Creating a DefaultTagger that tags every word as 'NN' (noun)
exptagger = DefaultTagger('NN')

# Tagging the provided sentences
tagged_sentences = exptagger.tag_sents([['Hi', ','], ['How', 'are', 'you', '?']])

# Printing the tagged sentences
print(tagged_sentences)