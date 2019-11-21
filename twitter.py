import os
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class TwitterClient(object):
    '''
      Generic Twitter Class for the app
    '''

    def __init__(self, query, retweets_only=False, with_sentiment=False):
        super().__init__()
        consumer_key = os.environ['TWITTER_SENTIMENT_ANALYSIS_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_SENTIMENT_ANALYSIS_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_SENTIMENT_ANALYSIS_ACCESS_TOKEN']
        access_token_SECRET = os.environ['TWITTER_SENTIMENT_ANALYSIS_ACCESS_TOKEN_SECRET']

        # Attempt to authenticate
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_SECRET)
            self.query = query
            self.retweets_only = retweets_only
            self.with_sentiment = with_sentiment
            self.api = tweepy.API(self.auth)
            self.tweet_count_max = 100
        except:
            print("Authentication Failed")
