import spacy
import en_core_web_sm

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Process the text
sen = nlp(u"I like to play cricket. I hated it in my childhood though")

# Print the entire sentence
print(sen.text)

# Print the part-of-speech tag and detailed tag for the 8th token
print(sen[7].pos_)
print(sen[7].tag_)
print(spacy.explain(sen[7].tag_))

# Loop through each token in the sentence and print its details
for word in sen:
    print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Process another sentence
sen = nlp(u'Can you google it?')
word = sen[2]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Process yet another sentence
sen = nlp(u'Can you search it on google?')
word = sen[5]
print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')

# Finding the number of POS tags in a sentence
sen = nlp(u"I like to play football. I hated it in my childhood though")
num_pos = sen.count_by(spacy.attrs.POS)
for k, v in sorted(num_pos.items()):
    print(f'{k}. {sen.vocab[k].text:{8}}: {v}')

# Visualizing parts of speech tags
from spacy import displacy
sen = nlp(u"I like to play football. I hated it in my childhood though")
displacy.serve(sen, style='dep', options={'distance': 120})