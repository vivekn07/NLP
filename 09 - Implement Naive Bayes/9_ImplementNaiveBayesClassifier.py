# Install necessary packages
# pip install pandas
# pip install scikit-learn
# pip install nltk

import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Download stopwords
nltk.download('stopwords')

# Load the data
sms_data = pd.read_csv("C:/Users/vivek/PycharmProjects/pythonProject_NLP2/spam.csv", encoding='latin-1')

# Rename columns for better understanding
sms_data.rename(columns={'v1': 'Category', 'v2': 'Message'}, inplace=True)

# Initialize PorterStemmer
stemming = PorterStemmer()
corpus = []

# Preprocess the data
for i in range(len(sms_data)):
    # Remove non-alphabetic characters
    s1 = re.sub('[^a-zA-Z]', ' ', sms_data['Message'][i])
    # Convert to lowercase
    s1 = s1.lower()
    # Split into words
    s1 = s1.split()
    # Stem words and remove stopwords
    s1 = [stemming.stem(word) for word in s1 if word not in set(stopwords.words('english'))]
    # Join words back into a single string
    s1 = ' '.join(s1)
    corpus.append(s1)

# Convert text data into numerical data
countvectorizer = CountVectorizer()
x = countvectorizer.fit_transform(corpus).toarray()
print(x)

# Extract target variable
y = sms_data['Category'].values
print(y)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y, random_state=2)

# Initialize Multinomial Naive Bayes model
multinomialnb = MultinomialNB()
# Train the model
multinomialnb.fit(x_train, y_train)

# Predict on test data
y_pred = multinomialnb.predict(x_test)
print(y_pred)

# Evaluate the model
print(classification_report(y_test, y_pred))
print("accuracy_score: ", accuracy_score(y_test, y_pred))