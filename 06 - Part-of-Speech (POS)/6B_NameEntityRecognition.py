# Install and upgrade spaCy
# pip install -U spacy

# Download the English model for spaCy
# python -m spacy download en_core_web_sm

import spacy

# Load the English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

# Process the text
text = ("Natural language processing (NLP) is an interdisciplinary subfield of computer science and information retrieval. "
        "It is primarily concerned with giving computers the ability to support and manipulate human language. "
        "It involves processing natural language datasets, such as text corpora or speech corpora, using either rule-based or probabilistic machine learning approaches.")
print("Original text: ", text, "\n")

# Create a spaCy document object
doc = nlp(text)

# Analyze syntax - extract noun phrases
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])

# Analyze syntax - extract verbs
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
