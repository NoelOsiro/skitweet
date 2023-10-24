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
    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
    ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
    if not CONSUMER_KEY or not CONSUMER_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        raise ValueError(
            "One or more Twitter API credentials are missing in the environment variables.")
    auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api
