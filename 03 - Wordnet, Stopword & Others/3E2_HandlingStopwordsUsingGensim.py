# pip install gensim nltk
import gensim
from gensim.parsing.preprocessing import remove_stopwords, STOPWORDS
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Sample text
text = "Viveksingh likes to play cricket, however he is not too fond of basketball."

# Remove stopwords using Gensim's remove_stopwords function
filtered_sentence = remove_stopwords(text)
print(filtered_sentence)

# Print the default set of stopwords in Gensim
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

# Add 'likes' and 'play' to the list of stopwords in Gensim
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))

# Tokenize the text
text_tokens = word_tokenize(text)

# Remove stopwords including the custom ones
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)

# Output:
# ['Harshad', 'cricket', ',', 'fond', 'basketball', '.']

# Remove the word 'not' from the set of stopwords in Gensim
sw_list = {"not"}
all_stopwords_gensim = STOPWORDS.difference(sw_list)

# Tokenize the text again
text_tokens = word_tokenize(text)

# Remove stopwords with the updated list
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]
print(tokens_without_sw)