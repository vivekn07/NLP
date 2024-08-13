from nltk.corpus import brown
from nltk.tag import RegexpTagger

# Get the first sentence from the 'news' category of the Brown corpus
test_sent = brown.sents(categories='news')[0]

# Define a regular expression tagger with patterns for different parts of speech
regexp_tagger = RegexpTagger([
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'),   # articles
    (r'.*able$', 'JJ'),                # adjectives
    (r'.*ness$', 'NN'),                # nouns formed from adjectives
    (r'.*ly$', 'RB'),                  # adverbs
    (r'.*s$', 'NNS'),                  # plural nouns
    (r'.*ing$', 'VBG'),                # gerunds
    (r'.*ed$', 'VBD'),                 # past tense verbs
    (r'.*', 'NN')                      # nouns (default)
])

# Print the tagger object
print(regexp_tagger)

# Tag the test sentence using the regular expression tagger
print(regexp_tagger.tag(test_sent))