import re 
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

curr_dir = os.path.dirname(os.path.realpath(__file__))
chords_file = f"{curr_dir}/data/chords.txt"
songs_file = f"{curr_dir}/data/songs.txt"
driver = webdriver.Chrome()

def get_url(artist,song):
    base_url = "https://www.e-chords.com/keyboards"
    
    # replace spaces with hyphen, make it lowercase, remove any other non-alphanumeric characters, replace accented characters with their non-accented counterparts
    artist = artist.replace(" ","-").lower()
    artist = ''.join(e for e in artist if e.isalnum() or e == "-")
    artist = artist.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u").replace("ñ","n")

    # regex to extract song name and remove any extra information (like ft. <artist>)
    pattern = re.compile(r"^([\w\s']+)(?:\s\(.+\))?(?:\s-\s.+)?(?:\s\(ft\. .+\))?$")

    # Extract the song name using the regex pattern
    match = pattern.match(song)
    if match is None:
        return
    else:
        song = match.group(1)
        # do the same processing as the artist name
        song = song.replace(" ","-").lower()
        song = song.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ü","u").replace("ñ","n")
        song = ''.join(e for e in song if e.isalnum() or e == "-")

    # create the url for the song
    return f"{base_url}/{artist}/{song}"

def scrape_song(artist,song):
    # get the url for the song
    chords_url = get_url(artist,song)
    # open it in the browser
    driver.get(chords_url)
    # find all the chord div elements
    chord_elements = driver.find_elements(By.CLASS_NAME, 'drawchord')
    # extract the text from each chord div element and store it in a text file
    with open(chords_file, "a") as f:
        for chord_element in chord_elements:
            f.write(chord_element.text + " ")
        f.write("\n")

def main():
    with open(songs_file, "r") as f:
        for line in f:
            artist, song = line.strip().split(",,")
            scrape_song(artist,song)

if __name__ == "__main__":
    main()


