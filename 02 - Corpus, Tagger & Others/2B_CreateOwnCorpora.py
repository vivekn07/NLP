import nltk
from nltk.corpus import PlaintextCorpusReader

# Download the 'punkt' tokenizer
nltk.download('punkt')

# Define the corpus root directory
corpus_root = r'C:\Users\vivek\PycharmProjects\Prac2\TextFiles'

# Create a PlaintextCorpusReader object
filelist = PlaintextCorpusReader(corpus_root, '.*')

# Print the list of files in the corpus
print('\n File list: \n')
print(filelist.fileids())
print(filelist.root)

# Display statistics for each text
print('\n\nStatistics for each text:\n')
print('AvgWordLen\tAvgSenLen\tNoOfTimesEachWordAppearsOnAvg\tFileName')

for fileid in filelist.fileids():
    num_chars = len(filelist.raw(fileid))
    num_words = len(filelist.words(fileid))
    num_sents = len(filelist.sents(fileid))
    num_vocab = len(set([w.lower() for w in filelist.words(fileid)]))

    avg_word_len = int(num_chars / num_words)
    avg_sent_len = int(num_words / num_sents)
    avg_word_freq = int(num_words / num_vocab)

    print(f'{avg_word_len}\t\t\t{avg_sent_len}\t\t\t{avg_word_freq}\t\t\t\t\t\t\t\t{fileid}')
