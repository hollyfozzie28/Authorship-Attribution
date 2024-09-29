import pandas as pd
import numpy as np
import matplotlib.pyplot as ply
import seaborn as sns
from pathlib import Path
from clean_tweet import CleanTweet

df = pd.read_csv("data/raw/raw_tweets_2.csv", on_bad_lines='skip')

# replace any AuthorID values equal to positive or negative infinity with NaN
# this error IDs were originated from the Twitter API fails
df['AuthorID'] = df['AuthorID'].replace([float('inf'), float('-inf')], float('nan'))
df['AuthorID'] = df['AuthorID'].fillna(0).astype(int)

# Separate data by author ID
authors = df.AuthorID.unique()
author_data = []
for author in authors:
    author_tweets = df[df['AuthorID'] == author]
    author_data.append(author_tweets)

# Remove authors with fewer than 10 tweets
author_data = [author for author in author_data if author.shape[0] >= 100]

# Combine the author data into a single DataFrame
df = pd.concat(author_data)

texts_new = []
for t in df.Tweets:
    cleaner = CleanTweet(t)
    clean_text = cleaner.deep_clean()
    texts_new.append(clean_text)

df['text_clean'] = texts_new

df.drop_duplicates("text_clean", inplace=True)

text_len = []
for text in df.text_clean:
    tweet_len = len(text.split())
    text_len.append(tweet_len)

df['text_len'] = text_len

base_path = Path(__file__).parent
repo_path = (base_path / "../data/processed").resolve()
df.to_csv(repo_path / 'cleaned_data_1.csv', index=False)


