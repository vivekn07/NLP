import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

# Download necessary NLTK data files
nltk.download('state_union')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Create our training and testing data
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# Train the Punkt tokenizer
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# Tokenize the sample text
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized[:2]:  # Process the first two tokenized sentences
            words = nltk.word_tokenize(i)  # Tokenize the sentence into words
            tagged = nltk.pos_tag(words)  # Tag each word with part of speech
            print(tagged)  # Print the tagged words
    except Exception as e:
        print(str(e))  # Print any exception that occurs

# Call the function to process content
process_content()