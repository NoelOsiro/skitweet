"""Main Script"""
from bot import TwitterBot
from helpers.twitter_auth import authenticate_twitter_api

# Replace with your actual Twitter API credentials
CONSUMER_KEY = "your_consumer_key"
CONSUMER_SECRET = "your_consumer_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

api = authenticate_twitter_api(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
bot = TwitterBot(api)

bot.tweet("Hello, Twitter!")
