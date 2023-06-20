import requests
import os
import pandas as pd
import config
import sys

if len(sys.argv) != 2:
    print("Usage: python spotify_scraper.py <playlist_id>")
    print("Playlist ID can be found in the URL of the playlist")
    print("Example: https://open.spotify.com/playlist/0K8DNHMwJaZmERK4FeaAOJ")
    sys.exit(1)

base_url = "https://api.spotify.com/v1"
curr_dir = os.path.dirname(os.path.realpath(__file__))
# songs_file = f"{curr_dir}/data/songs.txt"
songs_file = f"{curr_dir}/data/songs.csv"

def authenticate():
    # Spotify API call
    auth = {
        "grant_type": "client_credentials"
    }
    auth_req = requests.post(
        "https://accounts.spotify.com/api/token",
        auth=(config.CLIENT_ID, config.CLIENT_SECRET),
        data=auth 
        )

    access_token = auth_req.json()["access_token"]

    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    return headers

def get_tracks(playlist_id):
    # Get playlist tracks
    playlist_url = f"{base_url}/playlists/{playlist_id}/tracks"

    tracks = requests.get(playlist_url, headers=authenticate()).json()["items"]

    df = pd.DataFrame(columns=["artist", "song"])

    df["artist"] = [track["track"]["artists"][0]["name"] for track in tracks]
    df["song"] = [track["track"]["name"] for track in tracks]


    df.to_csv(songs_file, index=False)

def main():
    playlist_id = sys.argv[1]
    get_tracks(playlist_id)

if __name__ == "__main__":
    main()