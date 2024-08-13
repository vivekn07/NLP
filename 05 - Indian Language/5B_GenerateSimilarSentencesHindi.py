# Dictionary of synonyms
synonyms = {
    "खुश": ["प्रसन्न", "आनंदित", "खुशी"],
    "बहुत": ["अधिक", "बहुत ज्यादा", "काफी"]
}


# Function to generate similar sentences by replacing some words with synonyms
def generate_similar_sentences(input_sentence, num_sentences=5):
    similar_sentences = []

    # Replace some words with synonyms
    for word, word_synonyms in synonyms.items():
        for synonym in word_synonyms:
            modified_sentence = input_sentence.replace(word, synonym)
            similar_sentences.append(modified_sentence)

    # Return only the specified number of similar sentences
    return similar_sentences[:num_sentences]


# Input sentence in Hindi
input_sentence = "मैं आज बहुत खुश हूँ।"

# Generate similar sentences
similar_sentences = generate_similar_sentences(input_sentence)

# Print the original and similar sentences
print("Original sentence:", input_sentence)
print("Similar sentences:")
for sentence in similar_sentences:
    print("-", sentence)