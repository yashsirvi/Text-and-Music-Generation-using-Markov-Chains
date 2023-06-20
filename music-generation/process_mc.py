import random
import os
import pandas as pd

curr_dir = os.path.dirname(os.path.realpath(__file__))
chords_file = f"{curr_dir}/data/chords.csv"

def get_chord_blocks():
    df = pd.read_csv(chords_file).astype(str)
    chord_blocks={}
    for chords in df["chords"]:
        # convert to string
        chords = chords.split(" ")
        chords = list(filter(None, chords))
        for i in range(len(chords)):
            if chords[i] in chord_blocks:
                chord_blocks[chords[i%len(chords)]].append(chords[(i+1)%len(chords)])
            else:
                chord_blocks[chords[i%len(chords)]]=[chords[(i+1)%len(chords)]]
    return chord_blocks

def generate_chord_progression(initial_chord,length):
    chord_blocks = get_chord_blocks()
    progression=[]
    progression.append(initial_chord)
    for i in range(length):
        # append a random one
        progression.append(random.choice(chord_blocks[progression[i]]))
    return progression
