import spacy

# Load a blank English model
nlp = spacy.blank("en")

# Input string
text = "Mayday! Mayday! Officer prince reporting enemy artillery heading towards north"

# Create a doc object, which is a container for a sequence of Token objects
doc = nlp(text)

# Extract words from the doc object
words = [word.text for word in doc]

# Print the list of words
print(words)
