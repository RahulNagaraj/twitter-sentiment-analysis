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

        def set_query(self, query=''):
            self.query = query
        
        def set_retweet_checking(self, retweets_only=False):
            self.retweets_only = retweets_only
        
        def set_with_sentiment(self, with_sentiment=False):
            self.with_sentiment = with_sentiment

        def clean_tweet(self, tweet):
            return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

        def get_tweet_sentiment(self, tweet):
            analysis = TextBlob(self.clean_tweet(self, tweet))
            if analysis.sentiment.polarity > 0:
                return 'positive'
            elif analysis.sentiment.polarity == 0:
                return 'neutral'
            else:
                return 'negative'

        def get_tweets(self):
            tweets = []

            try:
                recd_tweets = self.api.search(q=self.query, count=self.tweet_count_max)

                if not recd_tweets:
                    pass
                for tweet in recd_tweets:
                    parsed_tweet = {}

                    parsed_tweet['text'] = tweet.text
                    parsed_tweet['user'] = tweet.user.screen_name

                    if (Self.with_sentiment):
                        parsed_tweet['with_sentiment'] = self.get_tweet_sentiment(self, tweet)
                    else:
                        parsed_tweet['with_sentiment'] = 'unavailable'

                    if tweet.retweet_count > 0 and self.retweets_only == 1:
                        if parsed_tweet not in tweets:
                            tweets.append(parsed_tweet)
                        else not self.retweets_only:
                            if parsed_tweet not in tweets:
                                tweets.append(parsed_tweet)
              
                  return tweets
              except tweepy.TweepError as e:
                  print("Error: " + str(e))

                


