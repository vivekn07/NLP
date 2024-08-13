# pip install nltk
import nltk

nltk.download('brown')
from nltk.corpus import brown

# Display file IDs of the Brown corpus
print('File IDs of Brown corpus:\n', brown.fileids())

# Pick out the first text and give it a short name
ca01 = brown.words('ca01')

# Display the first few words
# Displaying only the first 10 words for brevity
print('\nca01 has the following words:\n', ca01[:10])

# Total number of words in ca01
print('\nca01 has', len(ca01), 'words')

# Categories or files in the Brown corpus
print('\n\nCategories or files in Brown corpus:\n', brown.categories())

# Display other information about each text
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSenLen\tNoOfTimesEachWordAppearsOnAvg\tFileName')

for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set(w.lower() for w in brown.words(fileid)))

    avg_word_len = int(num_chars / num_words)
    avg_sent_len = int(num_words / num_sents)
    avg_word_freq = int(num_words / num_vocab)

    print(f'{avg_word_len}\t\t\t{avg_sent_len}\t\t\t{avg_word_freq}\t\t\t\t\t\t\t\t{fileid}')
