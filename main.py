from twitter_api import fetch_tweets
from sentiment import get_sentiment

def analyze_tweets(query, count=10):
    tweets = fetch_tweets(query, count)
    results = [{"tweet": tweet, "sentiment": get_sentiment(tweet)} for tweet in tweets]
    return results

if __name__ == "__main__":
    topic = input("Enter a topic to analyze sentiment: ")
    results = analyze_tweets(topic, count=10)

    for res in results:
        print(f"Tweet: {res['tweet']}\nSentiment: {res['sentiment']}\n{'-'*50}")
