#!/bin/bash 

# check if data/songs.csv exists 
if [ ! -f data/songs.csv ]; then
    python3 spotify_scraper.py
else
    echo "data/songs.csv already exists, would you like to overwrite it? (y/n)"
    read overwrite
    if [ $overwrite == "y" ]; then
        echo "Enter playlist ID: "
        read playlist_id
        python3 spotify_scraper.py $playlist_id
        python3 echords_scraper.py
    fi
fi

# check if data/chords.csv exists
if [ ! -f data/chords.csv ]; then
    python3 echords_scraper.py
fi




