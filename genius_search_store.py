import json
import requests
from google.cloud import storage
from config import GENIUS_ACCESS_TOKEN  # Securely import API token
from config import GENIUS_BUCKET  # Securely import GCS bucket name

# Google Cloud Storage settings
BUCKET_NAME = GENIUS_BUCKET  # Your actual bucket name
storage_client = storage.Client()

def search_song(song_name):
    """
    Fetch song data from the Genius API.

    Parameters:
        song_name (str): The name of the song to search for.

    Returns:
        list: A list of song results formatted for NDJSON.
    """
    base_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"}
    params = {"q": song_name}

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return [hit["result"] for hit in data["response"]["hits"]]  # Extract list of songs
    else:
        print(f"Error: {response.status_code}")
        return None

def save_to_gcs(song_name, song_list):
    """
    Save Genius API response data as NDJSON and upload to Google Cloud Storage.

    Parameters:
        song_name (str): The name of the song.
        song_list (list): List of JSON objects representing each song.
    """
    bucket = storage_client.bucket(BUCKET_NAME)
    file_name = f"raw_data/{song_name.replace(' ', '_')}.json"
    blob = bucket.blob(file_name)

    # Convert list of JSON objects to properly formatted NDJSON
    ndjson_data = "\n".join([json.dumps(song) for song in song_list])

    # Upload NDJSON file
    blob.upload_from_string(ndjson_data, content_type="application/json")

    print(f"✅ Data saved to GCS as NDJSON: gs://{BUCKET_NAME}/{file_name}")

if __name__ == "__main__":
    song_name = "Lose Yourself"
    song_data = search_song(song_name)

    if song_data:
        save_to_gcs(song_name, song_data)
