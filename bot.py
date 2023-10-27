import random
import tweepy
import json
from helpers.readFile import read_data_from_json, remove_images_in_folder
from helpers.tweet_gen import gen_first_tweet, gen_fourth_tweet, gen_second_tweet, gen_third_tweet
from helpers.twitter_auth import authenticate_twitter_api

class TwitterBot:
    """
    A Twitter bot class for posting tweets.

    Args:
        client (tweepy.Client): A Tweepy Client object for interacting with Twitter.

    Attributes:
        client (tweepy.Client): The Tweepy Client object for posting tweets.
    """

    def __init__(self, api_dic:dict):
        """
        Initialize a new TwitterBot instance.

        Args:
            client (tweepy.Client): A Tweepy Client object for interacting with Twitter.
        """
        self.api_dic = api_dic
        self.tweeted_entries = set() 
        
    def tweet(self):
        """
        Post a tweet thread based on data from a JSON entry.

        Returns:
            None
        """
        entries = read_data_from_json('output.json')

        # Choose a random entry that has not been tweeted before
        remaining_entries = [
            entry for entry in entries
            if entry['id'] not in self.tweeted_entries]
        if not remaining_entries:
            print("No more entries to tweet.")
            return

        entry = random.choice(remaining_entries)
        self.tweeted_entries.add(entry['id'])

        # Create the first tweet in the thread
        first_tweet_id = gen_first_tweet(self.api_dic, entry)

        # Create the second tweet in the thread
        second_tweet_id = gen_second_tweet(self.api_dic, entry, first_tweet_id)

        # Create the third tweet in the thread
        third_tweet_id = gen_third_tweet(self.api_dic, entry, second_tweet_id)

        # Create the fourth tweet in the thread
        fourth_tweet_id = gen_fourth_tweet(self.api_dic, entry, third_tweet_id)

        # Remove images in the 'images' folder
        remove_images_in_folder('images')
