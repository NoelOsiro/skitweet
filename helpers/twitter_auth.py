"""Authentication part"""
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

def authenticate_twitter_api():
    """
    Authenticate with the Twitter API using the provided credentials.

    Args:
        consumer_key (str): Twitter API consumer key.
        consumer_secret (str): Twitter API consumer secret.
        access_token (str): Twitter API access token.
        access_token_secret (str): Twitter API access token secret.

    Returns:
        tweepy.API: A Tweepy API object for interacting with Twitter.
    """
    CONSUMER_KEY = 'xHipDavldWpVzCEeFyTjI83k1'
    CONSUMER_SECRET = 'gTs6R7uUicTiFO7siFIJtHq45OO5kv9ihFzMfdEh12y0zgWjNh'
    ACCESS_TOKEN = '2419492390-aCkX0AwyTujMUcL2fnWo7nCv1JmAv7CNLxmUiyB'
    ACCESS_TOKEN_SECRET = 'cjdbpy1wsLqrBNzV2hNTJpHVcyakMnGMg3Ygw1ZhlKvHf'
    if not CONSUMER_KEY or not CONSUMER_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        raise ValueError(
            "One or more Twitter API credentials are missing in the environment variables.")
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
    )
    return client
