import unittest
import tweepy
from unittest.mock import patch
from helpers.twitter_auth import authenticate_twitter_api

class TestTwitterAuth(unittest.TestCase):
    @patch("os.getenv")
    def test_authenticate_twitter_api_success(self, mock_getenv):
        """
        Test successful authentication scenario.

        This test case simulates a scenario where all required environment variables
        are set correctly, and authentication should succeed.
        """
        mock_getenv.side_effect = lambda key: {
            "CONSUMER_KEY": "your_consumer_key",
            "CONSUMER_SECRET": "your_consumer_secret",
            "ACCESS_TOKEN": "your_access_token",
            "ACCESS_TOKEN_SECRET": "your_access_token_secret",
        }.get(key)

        api = authenticate_twitter_api()

        # Check if the authentication is successful
        self.assertIsInstance(api, tweepy.API)

    @patch("os.getenv")
    def test_authenticate_twitter_api_missing_variable(self, mock_getenv):
        """
        Test missing environment variable scenario.

        This test case simulates a scenario where one or more required environment
        variables are missing. It should raise a ValueError.
        """
        mock_getenv.side_effect = lambda key: {
            "CONSUMER_KEY": "your_consumer_key",
            "CONSUMER_SECRET": "your_consumer_secret",
            "ACCESS_TOKEN": None,
            "ACCESS_TOKEN_SECRET": "your_access_token_secret",
        }.get(key)

        with self.assertRaises(ValueError):
            api = authenticate_twitter_api()

    @patch("os.getenv")
    def test_authenticate_twitter_api_empty_variable(self, mock_getenv):
        """
        Test empty environment variable scenario.

        This test case simulates a scenario where one or more required environment
        variables are empty. It should raise a ValueError.
        """
        mock_getenv.side_effect = lambda key: {
            "CONSUMER_KEY": "",
            "CONSUMER_SECRET": "",
            "ACCESS_TOKEN": "",
            "ACCESS_TOKEN_SECRET": "",
        }.get(key)

        with self.assertRaises(ValueError):
            api = authenticate_twitter_api()

    @patch("os.getenv")
    def test_authenticate_twitter_api_invalid_variable(self, mock_getenv):
        """
        Test invalid environment variable scenario.

        This test case simulates a scenario where one or more required environment
        variables contain invalid values (e.g., not in the expected format). It should raise a ValueError.
        """
        mock_getenv.side_effect = lambda key: {
            "CONSUMER_KEY": "your_consumer_key",
            "CONSUMER_SECRET": "your_consumer_secret",
            "ACCESS_TOKEN": None,
            "ACCESS_TOKEN_SECRET": "your_access_token_secret",
        }.get(key)

        with self.assertRaises(ValueError):
            api = authenticate_twitter_api()

if __name__ == '__main__':
    unittest.main()
