import random
import tweepy
import json

class TwitterBot:
    """
    A Twitter bot class for posting tweets.

    Args:
        client (tweepy.Client): A Tweepy Client object for interacting with Twitter.

    Attributes:
        client (tweepy.Client): The Tweepy Client object for posting tweets.
    """

    def __init__(self, client):
        """
        Initialize a new TwitterBot instance.

        Args:
            client (tweepy.Client): A Tweepy Client object for interacting with Twitter.
        """
        self.client = client
        self.tweeted_entries = set() 

    def tweet(self, message):
        """
        Post a tweet to Twitter.

        Args:
            message (str): The text content of the tweet.

        Returns:
            tweepy.Status: The status object representing the posted tweet.
        """
        return self.client.create_tweet(text=message)

    def read_data_from_json(self, file_path):
        """
        Read data from a JSON file.

        Args:
            file_path (str): The path to the JSON file to read.

        Returns:
            list: A list of dictionaries, where each dictionary represents an entry from the JSON file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {file_path}")
        return []
    
    def tweet_thread_from_json_entry(self, entry):
        """
        Post a tweet thread based on data from a JSON entry.

        Args:
            entry (dict): A dictionary containing information for the tweet thread.

        Returns:
            None
        """
        # You can customize how you want to format the tweet thread using data from the entry.
        tweet_text = entry.get('title', 'Default tweet text if title is missing in entry')

        # Create the first tweet in the thread
        first_tweet = self.client.create_tweet(text=tweet_text)

        # Iterate through additional information in the entry and add tweets to the thread
        for key, value in entry.items():
            if key != 'title':
                tweet_text = f"{key}: {value}"
                self.client.create_tweet(text=tweet_text, in_reply_to_status_id=first_tweet.id)

    def tweet_random_thread(self, data):
        """
        Select a random entry from the data and tweet a thread about it.
        
        Args:
            data (list): A list of dictionaries, where each dictionary represents an entry.
        
        Returns:
            None
        """
        if not data:
            print("No data available for tweeting.")
            return

        # Shuffle the data to select a random entry
        random.shuffle(data)

        for entry in data:
            if entry['id'] not in self.tweeted_entries:
                self.tweeted_entries.add(entry['id'])
                self.tweet_thread_from_json_entry(entry)
                return