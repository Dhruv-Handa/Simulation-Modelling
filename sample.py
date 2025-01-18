import pandas as pd
import string

data = pd.read_csv('/Users/dhruvhanda/Desktop/Pantea Social Media/full-corpus-x.csv')
stopwords = ['the', 'and', 'a', 'to', 'in', 'of', 'is', 'for', 'on', 'it', 'this', 'at', 'with', 'as', 'that', 'by', 'an', 'from', 'was', 'are', 'or', 'not']

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return ' '.join(words)

data['CleanText'] = data['TweetText'].apply(clean_text)

all_words = ' '.join(data['CleanText']).split()
word_counts = pd.Series(all_words).value_counts()

top_words = word_counts.head(50)

print(top_words)