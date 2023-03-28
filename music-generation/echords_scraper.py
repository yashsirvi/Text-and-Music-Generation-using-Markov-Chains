from bs4 import BeautifulSoup
import requests
import re 
from spotify_scraper import get_tracks


def scrape_song(artist,song):

    base_url = "https://www.e-chords.com/keyboards"
    

    artist = artist.replace(" ","-").lower()
    artist = ''.join(e for e in artist if e.isalnum() or e == "-")
    artist = artist.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u").replace("ñ","n")

    pattern = re.compile(r"^([\w\s']+)(?:\s\(.+\))?(?:\s-\s.+)?(?:\s\(ft\. .+\))?$")

    # Extract the song name using the regex pattern
    match = pattern.match(song)
    if match is None:
        return
    else:
        song = match.group(1)
        song = song.replace(" ","-").lower()
        song = song.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u").replace("ñ","n")
        song = ''.join(e for e in song if e.isalnum() or e == "-")

    # create the url for the song
    chords_url = f"{base_url}/{artist}/{song}"

    # get the html of the page
    response = requests.get(chords_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # print(soup)
    # Find the div that contains the chord
    # Find all the divs that contain the chords
    chord_divs = soup.find_all('div', {'class': 'drawchord'})

    if chord_divs is None:
        print("chord = N/A")
    else:
        for chord_div in chord_divs:
            chord = chord_div.get_text().strip()
            print(f"chord = {chord}")

    # # Extract the text content of each div and store it in a list
    # chords = []
    # for chord_div in chord_divs:
    #     chord = chord_div.get_text().strip()
    #     chords.append(chord)

    # # Extract the text content of the div
    # if chord_div is None:
    #     print("chord = N/A")
    # else:
    #     chord = chord_div.get_text().strip()
    #     print(f"chord = {chord}")

    # Print the chord
    # print(chord)


def main():

    # scrape_song("The Beatles","Yesterday")

    # get the artist and song names from the text file
    with open("./data/songs.txt", "r") as f:
        for line in f:
            artist, song = line.strip().split(",,")
            scrape_song(artist,song)

if __name__ == "__main__":
    print("Starting echords scraper")
    main()


