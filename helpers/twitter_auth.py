import os
import tweepy
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

def authenticate_twitter_api() -> Dict:
    """
    Authenticate with the Twitter API using the provided credentials.

    Returns:
        api_dic: A Tweepy dict with API, Client objects for interacting with Twitter.
    """
    CONSUMER_KEY='M7EJl8aOSZXcp8U5tT0AMxJAU'
    CONSUMER_SECRET='NI3u0McaVniR4x02qGdYFA7ugcfdWnuIsgxipzukWXLOsd0XyX'
    ACCESS_TOKEN='2419492390-gGLLn0pmow0CZ609velznNGdWvVvP5efhkoIKZ9'
    ACCESS_TOKEN_SECRET='x1Nay7E6CDyVS9WPtRFqiJVJ43D40aYwY6KjK2Kzq2ZDr'

    if not CONSUMER_KEY or not CONSUMER_SECRET or not ACCESS_TOKEN or not ACCESS_TOKEN_SECRET:
        raise ValueError(
            "One or more Twitter API credentials are missing in the environment variables.")
    
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    client = tweepy.Client(
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET
    )
    return {'api': api, 'client': client}
