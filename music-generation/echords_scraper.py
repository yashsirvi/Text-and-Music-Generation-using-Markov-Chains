from bs4 import BeautifulSoup
import requests
import re 
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

def get_url(artist,song):
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
    return f"{base_url}/{artist}/{song}"

def scrape_song(artist,song):

    chords_url = get_url(artist,song)
    print(chords_url)

    driver.get(chords_url)


    # div_element = driver.find_element(By.ID, 'thechord_0')

    # print(div_element.text)

    # find all the chord div elements
    chord_elements = driver.find_elements(By.CLASS_NAME, 'drawchord')

    # extract the text from each chord div element and store it in a text file
    with open("./data/chords.txt", "a") as f:
        for chord_element in chord_elements:
            f.write(chord_element.text + " ")
        f.write("\n")
            

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


