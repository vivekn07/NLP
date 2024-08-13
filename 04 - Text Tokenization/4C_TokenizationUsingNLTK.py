import nltk
from nltk import tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('words')

# Paragraph to be tokenized
para = "Hello! My name is Viveksingh. Today we will be learning NLTK."

# Sentence tokenization
sents = tokenize.sent_tokenize(para)
print("\n================Sentence tokenization================\n\n", sents)


# Word tokenization
print("\n=================Word tokenization===================\n")
for index in range(len(sents)):
    # Tokenize each sentence into words
    words = tokenize.word_tokenize(sents[index])
    print(words)
