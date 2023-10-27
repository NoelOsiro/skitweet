"""Generate tweet thread per entry"""
from helpers.readFile import download_and_save_image


def gen_first_tweet(api_dic, entry) -> str:
    """
    First tweet of the thread based on data from a JSON entry.

    Args:
        entry (dict): A dictionary containing information for the tweet thread.
        api_dic (dict): A dictionary containing client and API authentication.

    Returns:
        str: Tweet ID of the first tweet in the thread.
    """
    download_and_save_image(entry['img_url'], 'image.jpg')
    media_id = api_dic['api'].media_upload(filename='./images/image.jpg').media_id_string
    tweet_text = f"📢 Project Name: {entry['title']}\n📋{entry['description']}."
    first_tweet = api_dic['client'].create_tweet(text=tweet_text, media_ids=[media_id])
    print('First Tweet sent ✅')
    return str(first_tweet.id)

def gen_second_tweet(api_dic, entry, tweet_id) -> str:
    """
    Second tweet of the thread based on data from a JSON entry.

    Args:
        entry (dict): A dictionary containing information for the tweet thread.
        api_dic (dict): A dictionary containing client and API authentication.
        tweet_id (dict): A string containing first tweet id.

    Returns:
        str: Tweet ID of the second tweet in the thread.
    """
    location_info = f"🌍 Location: This project serves {entry['country']},{entry['subregion']},{entry['region']}"
    sdgs_info = f"🌱 Sustainable Development Goals (SDGs): {', '.join(entry['sdg'])}. This project aligns with key global development goals, contributing to a sustainable future."
    second_tweet = api_dic['client'].create_tweet(text=location_info + sdgs_info, in_reply_to_status_id=tweet_id)
    print('Second Tweet sent ✅')
    return str(second_tweet.id)

def gen_third_tweet(api_dic, entry, tweet_id) -> str:
    """
    Third tweet of the thread based on data from a JSON entry.

    Args:
        entry (dict): A dictionary containing information for the tweet thread.
        api_dic (dict): A dictionary containing client and API authentication.
        tweet_id (dict): A string containing second tweet id.

    Returns:
        str: Tweet ID of the second tweet in the thread.
    """
    use_info = f"🌍 Use case: Intended for {entry['use_case']} The project utilizes: {', '.join(entry['technology'])}."
    third_tweet = api_dic['client'].create_tweet(text=use_info , in_reply_to_status_id=tweet_id)
    print('Third Tweet sent ✅')
    return str(third_tweet.id)

def gen_fourth_tweet(api_dic, entry, tweet_id) -> str:
    """
    Fourth tweet of the thread based on data from a JSON entry.

    Args:
        entry (dict): A dictionary containing information for the tweet thread.
        api_dic (dict): A dictionary containing client and API authentication.
        tweet_id (dict): A string containing second tweet id.

    Returns:
        str: Tweet ID of the fourth tweet in the thread.
    """
    use_info = f"🔗 Source: Learn more about this project on the official website: {entry['source']}. Stay informed and support this vital humanitarian effort!"
    fourth_tweet = api_dic['client'].create_tweet(text=use_info , in_reply_to_status_id=tweet_id)
    print('Third Tweet sent ✅')
    return str(fourth_tweet.id)


