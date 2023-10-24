"""Authentication part"""
import tweepy

def authenticate_twitter_api(
        consumer_key:str,
        consumer_secret:str,
        access_token:str,
        access_token_secret:str):
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
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
