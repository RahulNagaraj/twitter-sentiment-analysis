# Server

import os
from flask import Flask, request, render_template, jsonify
from twitter import TwitterClient

app = Flask(__name__)
# Setup the client
api = TwitterClient('@NagarajmvRahul')

def str_to_bool(s):
    return s.lower() in ['yes', 'true', 1, 't']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tweets')
def tweets():
    retweets_only = request.args.get('retweets_only')
    api.set_retweet_checking(str_to_bool(retweets_only.lower()))
    with_sentiment = request.args.get('with_sentiment')
    api.set_with_sentiment(str_to_bool(with_sentiment.lower()))
    query = request.args.get('query')
    api.set_query(query)

    tweets = api.get_tweets()
    return jsonify({
      'data': tweets,
      'count': len(tweets)
    })

port = int(os.environ.get('PORT', 5000))
app.run(host="0.0.0.0", port=port, debug=True)
