import tweepy
from textblob import TextBlob 

consumer_key = 'dJMoBeYmK4ZJ7nCIUXnm1SFGs'
consumer_secret = 'lP1PEsUHOWPyhnO3jnnFIzTbo3Qinbi6ZtPgYM3xVL4x7EfRZ7'

access_token = '466621281-iHa07jzlJfOmLz26l0OWM52PenP9oiSrsSUKVTWP'
access_token_secret = 'Jypzx9hfa0kxWQl1BMZz4zTRoGZOqkpKiBqySOaDq3r9H'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets= api.search('Narendra Modi')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)



