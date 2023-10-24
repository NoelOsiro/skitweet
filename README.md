# Skitweet 🤖

A Python Twitter bot that posts tweets using Tweepy, designed with Object-Oriented Programming (OOP) and Test-Driven Development (TDD) principles. 🐍🐦

## Getting Started 🚀

These instructions will help you set up the project and get your Twitter bot up and running.

### Prerequisites 📋

- Python 3.x
- Tweepy library (install via `pip`)
- Twitter API credentials (consumer key, consumer secret, access token, access token secret)

### Installation 🛠️

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/TwitterBot.git
   cd TwitterBot
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```

3. Install the required packages:

   ```bash
   pip install tweepy
   ```

4. Authenticate your Twitter API by replacing the placeholders in `twitter_auth.py` with your own credentials.

## Running Tests 🧪

To run the unit tests, use the following command:

```bash
python -m unittest test_bot
```

Make sure all tests pass before moving forward.

## Usage 🤖

1. In a separate script, you can create a TwitterBot instance, authenticate with your Twitter API credentials, and use it to post tweets, retweet, follow users, and more.

   ```python
   from bot import TwitterBot
   from twitter_auth import authenticate_twitter_api

   api = authenticate_twitter_api(consumer_key, consumer_secret, access_token, access_token_secret)
   bot = TwitterBot(api)

   bot.tweet("Hello, Twitter!")
   ```

2. Customize your bot's functionality to suit your specific needs.

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 🙏

- [Tweepy](https://www.tweepy.org/): The easy-to-use Python library for accessing the Twitter API.
- Emoji icons from [Emojipedia](https://emojipedia.org/).

Happy botting! 🚀🐦
