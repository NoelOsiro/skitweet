"""Bot class file"""
import tweepy

class TwitterBot:
    """
    A Twitter bot class for posting tweets.

    Args:
        api (tweepy.API): A Tweepy API object for interacting with Twitter.

    Attributes:
        api (tweepy.API): The Tweepy API object for posting tweets.
    """

    def __init__(self, api):
        """
        Initialize a new TwitterBot instance.

        Args:
            api (tweepy.API): A Tweepy API object for interacting with Twitter.
        """
        self.api = api

    def tweet(self, message):
        """
        Post a tweet to Twitter.

        Args:
            message (str): The text content of the tweet.

        Returns:
            tweepy.Status: The status object representing the posted tweet.
        """
        return self.api.update_status(message)
