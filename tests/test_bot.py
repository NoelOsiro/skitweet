import unittest
from unittest.mock import MagicMock
from bot import TwitterBot
from helpers.twitter_auth import authenticate_twitter_api

class TestTwitterBot(unittest.TestCase):
    def test_tweet(self):
        api_mock = MagicMock()
        bot = TwitterBot(api_mock)
        bot.tweet("Hello, Twitter!")
        api_mock.update_status.assert_called_with("Hello, Twitter!")

if __name__ == '__main__':
    unittest.main()
