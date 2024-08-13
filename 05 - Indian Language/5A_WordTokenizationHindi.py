# pip install indic-nlp-library
import sys
from indicnlp import common

# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME = r"indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES = r"indic_nlp_resources"

# Add library to Python path
sys.path.append(r'{}\src'.format(INDIC_NLP_LIB_HOME))

# Set environment variable for resources folder
common.set_resources_path(INDIC_NLP_RESOURCES)

from indicnlp.tokenize import indic_tokenize

# Input string in Hindi
indic_string = 'सुनो, कुछ आवाज़ आ रही है। फोन?'

# Print the input string
print('Input String: {}'.format(indic_string))

# Tokenize the input string and print each token
print('Tokens: ')
for t in indic_tokenize.trivial_tokenize(indic_string):
    print(t)
