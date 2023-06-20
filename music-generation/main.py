from play_song import *
from process_mc import *

import argparse 

def parse_args():
    parser = argparse.ArgumentParser(description="Generate chord progression and play it")
    parser.add_argument("--initial_chord", type=str, default="F", help="Initial chord")
    parser.add_argument("--progression_length", type=int, default=10, help="Length of chord progression")
    parser.add_argument("--instrument", type=str, default="Electric Piano 1", help="Instrument to play chord progression, for a list of instruments see https://soundprogramming.net/file-formats/general-midi-instrument-list/")
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    chords = generate_chord_progression(args.initial_chord,args.progression_length)
    print(chords)
    chords = [Chord(chord) for chord in chords]
    create_midi(chords,args.instrument)
    play_midi()

if __name__ == "__main__":
    main()



    
