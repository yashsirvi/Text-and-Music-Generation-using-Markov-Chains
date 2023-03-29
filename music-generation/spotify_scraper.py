import requests
import os

base_url = "https://api.spotify.com/v1"
curr_dir = os.path.dirname(os.path.realpath(__file__))
songs_file = f"{curr_dir}/data/songs.txt"

def authenticate():
    # Spotify API call
    client_id = "42d7ee2a8314487087feee9255476dab"
    client_secret = "5ca3de05d8554ffd9d94821bd567beb5"
    auth = {
        "grant_type": "client_credentials"
    }
    auth_req = requests.post(
        "https://accounts.spotify.com/api/token",
        auth=(client_id, client_secret),
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

    with open(songs_file, "a") as f:
        for track in tracks:
            # get artist and song names
            artist = track["track"]["artists"][0]["name"]
            song = track["track"]["name"]
            
            # write it to the file
            f.write(f"{artist},,{song}\n")

def main():
    playlist_id = "0K8DNHMwJaZmERK4FeaAOJ"
    get_tracks(playlist_id)

if __name__ == "__main__":
    main()