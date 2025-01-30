import tweepy
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET

def authenticate_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)

def fetch_tweets(query, count=100):
    api = authenticate_twitter()
    tweets = api.search_tweets(q=query, count=count, lang="en", tweet_mode="extended")
    return [tweet.full_text for tweet in tweets]
