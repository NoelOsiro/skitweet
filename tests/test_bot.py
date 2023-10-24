import unittest
from unittest.mock import MagicMock
from bot import TwitterBot
from helpers.twitter_auth import authenticate_twitter_api

class TestTwitterBot(unittest.TestCase):
    def test_tweet(self):
        # Mock the Tweepy API call to avoid actual posting
        api_mock = MagicMock()
        bot = TwitterBot(api_mock)

        # Call the tweet method
        bot.tweet("Hello, Twitter!")

        # Check if the mock API call was made
        api_mock.update_status.assert_called_with("Hello, Twitter!")

if __name__ == '__main__':
    unittest.main()
