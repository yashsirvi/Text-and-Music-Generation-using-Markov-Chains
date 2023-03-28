import requests
import json
from spotify_scraper import get_tracks
from ultimateguitar_scraper import *

#! Currently using the following playlist: https://open.spotify.com/playlist/0K8DNHMwJaZmERK4FeaAOJ
playlist_id = "0K8DNHMwJaZmERK4FeaAOJ"

# do get_tracks if text file doesnt exist already
get_tracks(playlist_id)




    
