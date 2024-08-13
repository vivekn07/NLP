import nltk
from collections import defaultdict

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Tokenize the text into words
text = nltk.word_tokenize("Viveksingh likes to play cricket. Viveksingh does not like to play with hearts.")

# Perform POS tagging on the tokenized text
tagged = nltk.pos_tag(text)
print(tagged)

# List to store noun words
addNounWords = []

# Iterate through the tagged words to find nouns
for word, tag in tagged:
    if tag in ('NN', 'NNS', 'NNPS', 'NNP'):
        addNounWords.append(word)

print(addNounWords)

# Dictionary to store the frequency of each noun
temp = defaultdict(int)

# Count the frequency of each noun
for noun in addNounWords:
    temp[noun] += 1

# Find the noun with the maximum frequency
res = max(temp, key=temp.get)

# Print the result
print("Word with maximum frequency: " + str(res))