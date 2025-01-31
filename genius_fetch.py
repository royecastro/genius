import requests  # Library for making HTTP requests
from config import GENIUS_ACCESS_TOKEN  # Import the access token securely

# STEP 1: AUTHENTICATION - Provide your Genius API access token
ACCESS_TOKEN = GENIUS_ACCESS_TOKEN  # Replace with your actual token


def search_song(song_name):
    """
    This function searches for a song on Genius using the Genius API.

    Parameters:
        song_name (str): The name of the song to search for.

    Returns:
        dict: The JSON response containing song search results.
    """

    # STEP 2: DEFINE API ENDPOINT
    base_url = "https://api.genius.com/search"  # Genius search endpoint

    # STEP 3: SET REQUEST HEADERS
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"  # API authentication
    }

    # STEP 4: SET REQUEST PARAMETERS
    params = {
        "q": song_name  # Search query for the song
    }

    # STEP 5: MAKE THE API CALL
    response = requests.get(base_url, headers=headers, params=params)

    # STEP 6: HANDLE RESPONSE
    if response.status_code == 200:
        data = response.json()  # Parse response as JSON
        return data  # Return the retrieved song data
    else:
        print(f"Error: {response.status_code}")  # Print error if request fails
        return None  # Return nothing in case of failure


# STEP 7: TEST THE FUNCTION
if __name__ == "__main__":
    song_data = search_song("Lose Yourself")  # Example search query
    print(song_data)  # Print the fetched data
