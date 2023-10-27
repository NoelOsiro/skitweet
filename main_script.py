"""Main Script"""
import os
from bot import TwitterBot
from helpers.twitter_auth import authenticate_twitter_api

api = authenticate_twitter_api()
bot = TwitterBot(api)

bot.tweet()
