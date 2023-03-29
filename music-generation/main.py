from play_song import *
from process_mc import *

def main():
    initial_chord = "F" 
    progression_length = 10
    instrument = "Electric Piano 1"
    chords = generate_chord_progression(initial_chord,progression_length)
    print(chords)
    chords = [Chord(chord) for chord in chords]
    create_midi(chords,instrument)
    play_midi()

if __name__ == "__main__":
    main()



    
