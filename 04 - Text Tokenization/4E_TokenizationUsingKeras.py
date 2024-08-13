# pip install --upgrade keras
# pip install tensorflow

import tensorflow as tf

# Create a string input
text = "Tokenization using Keras and Tensorflow"

# Tokenize the text
tokens = tf.keras.preprocessing.text.text_to_word_sequence(text)

# Print the list of tokens
print(tokens)