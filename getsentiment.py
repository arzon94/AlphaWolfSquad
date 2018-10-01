print("\nConnecting to Twitter's API...")

import os
import tweepy
from textblob import TextBlob

def bitcoin(rate='30min'):
	print(os.environ['CONSUMER_KEY'])

	consumer_key = os.environ['CONSUMER_KEY']
	consumer_secret_key = os.environ['CONSUMER_SECRET_KEY']

	access_token = os.environ['ACCESS_TOKEN']
	access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	public_tweets = api.search('Bitcoin', count=150)

	polCount = 0
	polSum = 0
	tweetcount = 20
	counter = 0
	sentimentArray = []
	dateArray = []
	if rate == '30min':
		tweetcount = 10
	for tweet in public_tweets:
		analysis = TextBlob(tweet.text)
		counter += 1
		if(counter < tweetcount):
			polSum = polSum + analysis.sentiment.polarity
		else:
			sentimentArray.append(polSum/counter*10)
			dateArray.append(tweet.created_at)
			counter = 0
			polSum = 0
		polCount = polCount + 1
		
	polAvg = (polSum / polCount)
	return(sentimentArray, polAvg, dateArray)
	# return("Average sentiment for %s: %f" %('Bitcoin', polAvg))