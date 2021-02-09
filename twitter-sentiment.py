#!/usr/bin/python3

from __future__ import unicode_literals
from decimal import *
from itertools import islice
from termcolor import colored
from textblob import TextBlob
from TwitterSearch import TwitterSearch,TwitterSearchException,TwitterUserOrder
import argparse
import os
import re

# define common outputs for sentiment scores
positive = colored('positive 📈', 'green')
neutral  = colored('neutral  😐', 'yellow')
negative = colored('negative 📉', 'red')

# create TwitterSearch object
# TODO add error handling and prompt for missing environment vars
ts = TwitterSearch(
	consumer_key = os.getenv('CONSUMER_KEY'),
	consumer_secret = os.getenv('CONSUMER_SECRET'),
	access_token = os.getenv('ACCESS_TOKEN'),
	access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
)

# set up command line arguments
parser = argparse.ArgumentParser(description='Displays sentiment analysis for a given user on Twitter.')
parser.add_argument('username', help='a Twitter username (ex: jack)')
parser.add_argument('--limit', metavar='X', type=int, default=100, help='limit the number of tweets returned (default: 100)')
parser.add_argument('--verbose', action='store_true', default=False, help='show individual tweets')
parser.add_argument('--debug', action='store_true', default=False, help='show extra output')
args = parser.parse_args()

# create a TwitterUserOrder using the command line arg as the query
tuo = TwitterUserOrder(args.username)

# start an index for counting the processed tweets
index = 0

# start a summary of sentiment scores for later averaging
sum_sentiment = 0

try:
	# ask Twitter for the timeline
	for tweet in islice(ts.search_tweets_iterable(tuo), 0, args.limit):
		
		index = index + 1

		# scrub usernames, special characters and URLs from tweet
		cleanTweet = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet['text'])

		# sentiment analysis using TextBlob
		analysis = TextBlob(cleanTweet)

		# define human friendly sentiment scores
		if analysis.sentiment.polarity > 0:
			score = positive
		elif analysis.sentiment.polarity == 0:
			score = neutral
		else:
			score = negative

		# raw sentiment score
		sentiment = analysis.sentiment.polarity

		# create a working sum of sentiment scores for averaging
		sum_sentiment = sum_sentiment + sentiment

		# current average
		avg_sentiment = sum_sentiment / index

		if args.verbose == True or args.debug == True:
			print('@%s tweeted: %s' % (tweet['user']['screen_name'], tweet['text']))
			if args.debug == True:
				print(f'scrubbed tweet: {cleanTweet}')
			print(f'sentiment: {score} ({sentiment:.2f})')
			if args.debug == True:
				print(f'avg_sentiment: {avg_sentiment:.2f} (sum_sentiment: {sum_sentiment:.4f}, index: {index})')
			print('----')

except TwitterSearchException as e:
	print(e)
	raise SystemExit()

# average sentiment for all processed tweets
if avg_sentiment > 0:
	avg_score = positive
elif avg_sentiment == 0:
	avg_score = neutral
else:
	avg_score = negative
print(f'\n\x1B[3maverage\nsentiment:\x1B[23m {avg_score} ({avg_sentiment:.2f})')

print('====')
