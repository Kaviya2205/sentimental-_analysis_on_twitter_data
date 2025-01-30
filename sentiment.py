from textblob import TextBlob
from preprocess import clean_text

def get_sentiment(text):
    text = clean_text(text)
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"
