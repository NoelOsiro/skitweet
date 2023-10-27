"""Read entries from file"""
import json
import os
import requests
import time

def read_data_from_json(file_path):
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

def download_and_save_image(url, filename, max_retries=3, retry_delay=5):
    """
    Download an image from a URL and save it in the 'images' folder with retries.

    Args:
        url (str): The URL of the image to download.
        filename (str): The name of the file to save the image as.
        max_retries (int): The maximum number of retry attempts (default is 3).
        retry_delay (int): The delay between retry attempts in seconds (default is 5).

    Returns:
        None

    Raises:
        Exception: If the download or file-saving process fails even after retries.
    """
    if not os.path.exists('images'):
        os.makedirs('images')

    for attempt in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join('images', filename), 'wb') as file:
                file.write(response.content)
            print(f"Image saved as {filename} in the 'images' folder.")
            return  # Successful download, exit the loop
        else:
            if attempt < max_retries - 1:
                print(f"Failed to download image from {url} (HTTP status code {response.status_code}). Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                raise Exception(f"Failed to download image from {url} after {max_retries} retries (HTTP status code {response.status_code}).")


def remove_images_in_folder(folder_path='images'):
    """
    Remove all image files in the specified folder.

    Args:
        folder_path (str): The path to the folder containing the image files. Default is 'images'.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified folder does not exist.
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path) and file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Check if the file is an image (you can add more image extensions if needed)
            os.remove(file_path)
            print(f"Removed image: {file}")