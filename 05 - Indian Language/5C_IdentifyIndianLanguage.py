# pip install langid
import nltk
import langid

# Download necessary NLTK data
nltk.download('punkt')

def identify_language(text):
    # Classify the language of the given text
    lang, _ = langid.classify(text)
    return lang

# Identify the language from the given text
language = identify_language("नमस्ते, आप कैसे हैं?")
print("Identified language:", language)  # Print the identified language