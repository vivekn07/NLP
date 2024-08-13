# Not running


# Import the MaltParser from nltk.parse.malt
from nltk.parse.malt import MaltParser

# Initialize the MaltParser with the path to the MaltParser directory and the model file
mp = MaltParser('maltparser-1.7.2', 'engmalt.linear-1.7.mco')

# Parse a sentence and get the parse tree
t = mp.parse_one('I saw a bird from my window.'.split()).tree()

# Print the parse tree
print(t)

# Draw the parse tree
t.draw()
