import nltk
# Import the RegexpTokenizer class from nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Create a reference variable for the RegexpTokenizer class
# The pattern '\s+' matches one or more whitespace characters
# The 'gaps=True' parameter indicates that the pattern matches gaps between tokens
tk = RegexpTokenizer(r'\s+', gaps=True)

# Create a string input
text = "Hi I am Viveksingh Negi"

# Use the tokenize method to split the string into tokens based on the pattern
tokens = tk.tokenize(text)

# Print the list of tokens
print(tokens)