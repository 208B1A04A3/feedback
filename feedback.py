#@title
#with input
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def get_sentiment(review):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        pos.append(review)
        return 'Positive'
    elif compound_score <= -0.05:
        neg.append(review)
        return 'Negative'
    else:
        return 'Neutral'

# Take user input for the review
review = input("Enter your review: ")
pos,neg=[],[]

# Analyze the sentiment of the review
sentiment = get_sentiment(review)
#print(f"Review: {review}")
#print(f"Sentiment: {sentiment}")
print('Postive feedback',pos)
print('Negative feedback',neg)