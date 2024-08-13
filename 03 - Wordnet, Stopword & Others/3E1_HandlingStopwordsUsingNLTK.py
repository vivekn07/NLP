import nltk
from nltk.corpus import stopwords

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize

# Sample text
text = "the quick brown fox jumps over the lazy dog but not a cat"

# Tokenize the text
text_tokens = word_tokenize(text)

# Remove stopwords from the tokenized text
tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
print(tokens_without_sw)

# Add a custom stopword
all_stopwords = stopwords.words('english')
all_stopwords.append('play')

# Tokenize the text again
text_tokens = word_tokenize(text)

# Remove stopwords including the custom one
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)

# Remove a specific stopword from the list
all_stopwords.remove('not')

# Tokenize the text again
text_tokens = word_tokenize(text)

# Remove stopwords with the updated list
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)