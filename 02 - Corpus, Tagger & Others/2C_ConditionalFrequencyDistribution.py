# Import necessary libraries
import nltk
from nltk.corpus import brown, inaugural, udhr

# Download necessary NLTK data
nltk.download('brown')
nltk.download('inaugural')
nltk.download('udhr')

# Process a sequence of pairs
text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]

# Create a Conditional Frequency Distribution (CFD) for genres and words in the Brown corpus
fd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

# Create a list of (genre, word) pairs for 'news' and 'romance' categories
genre_word = [
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
]

# Print the length of the genre_word list and the first and last 4 elements
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])

# Create a CFD from the genre_word list
cfd = nltk.ConditionalFreqDist(genre_word)

# Print the CFD, its conditions, and the frequency distributions for 'news' and 'romance'
print(cfd)
print(cfd.conditions())
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))

# Create a CFD for the words 'america' and 'citizen' in the Inaugural corpus
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

# Define a list of languages from the UDHR corpus
languages = [
    'Chickasaw', 'English', 'German_Deutsch',
    'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik'
]

# Create a CFD for the length of words in different languages from the UDHR corpus
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)

# Tabulate the CFD for 'English' and 'German_Deutsch' with word lengths up to 10, cumulative
cfd.tabulate(conditions=['English', 'German_Deutsch'], samples=range(10), cumulative=True)