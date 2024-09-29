import tweepy
import pandas as pd
import numpy as np
from constants import BEARER_TOKEN
from datetime import datetime

client = tweepy.Client(wait_on_rate_limit=True, bearer_token=BEARER_TOKEN)

# Start of the 2010 season
start_time = '2010-10-28T00:00:00Z'

# All star weekend break
end_time = '2023-02-20T00:00:00Z'

queries = ["from:KingJames -is:retweet", "from:Dame_Lillard -is:retweet",
           "from:KDTrey5 -is:retweet", "from:StephenCurry30 -is:retweet",
           "from:luka7doncic -is:retweet", "from:jaytatum0 -is:retweet",
           "from:Giannis_An34 -is:retweet", "from:kawhileonard -is:retweet", 
           "from:JHarden13 -is:retweet", "from:JoelEmbiid -is:retweet",
           "from:Money23Green -is:retweet", "from:SDinwiddie_25 -is:retweet", 
           "from:gb3elite -is:retweet","from:AndreDrummond -is:retweet", "from:BucketsONeale00 -is:retweet"]

# Check if there is an existing csv file, if not create a new one
try:
    data = pd.read_csv('data/raw/raw_tweets_5.csv', index_col=0)
    last_query = data['AuthorID'].iloc[-1]
    print(f"Existing data found. Restarting from {start_time}")
except FileNotFoundError:
    data = pd.DataFrame(columns=['Tweets', 'AuthorID', 'CreatedAt'])


for query in queries:
    counter = 0
    for tweet in tweepy.Paginator(client.search_all_tweets, query=query, 
                                tweet_fields=['author_id', 'created_at'],
                                start_time=start_time, end_time=end_time,
                                max_results=100).flatten(limit=20000):
        counter += 1
        data = data.append({'Tweets': tweet.text, 'AuthorID': tweet.author_id, 'CreatedAt': tweet.created_at}, 
                           ignore_index=True)
    
    print(f"Query '{query}' done. {counter} tweets appended. Total tweets: {len(data)}")

print(f"All queries done. Total tweets: {len(data)}")
data.to_csv('data/raw/raw_tweets_5.csv', mode='a', header=(not data.index.any()))