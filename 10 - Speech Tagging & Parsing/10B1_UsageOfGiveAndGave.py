import nltk

# Define a function to identify specific verb phrases (VP)
def give(t):
    return (t.label() == 'VP' and len(t) > 2 and t[1].label() == 'NP'
            and (t[2].label() == 'PP-DTV' or t[2].label() == 'NP')
            and ('give' in t[0].leaves() or 'gave' in t[0].leaves()))

# Define a function to convert a tree to a sentence string
def sent(t):
    return ' '.join(token for token in t.leaves() if token[0] not in '*-0')

# Define a function to print a node with a specified width
def print_node(t, width):
    output = "%s %s: %s / %s: %s" % (
        sent(t[0]), t[1].label(), sent(t[1]), t[2].label(), sent(t[2])
    )
    if len(output) > width:
        output = output[:width] + "..."
    print(output)

# Download necessary NLTK data files
nltk.download('treebank')

# Iterate over parsed sentences in the treebank corpus
for tree in nltk.corpus.treebank.parsed_sents():
    for t in tree.subtrees(give):  # Find subtrees matching the 'give' function
        print_node(t, 72)  # Print the node with a width limit of 72 characters
