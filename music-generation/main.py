from play_song import *
from process_mc import *

def main():
    initial_chord = "C"
    progression_length = 10
    instrument = "French Horn"
    print(chords)
    chords = generate_chord_progression(initial_chord,progression_length)
    chords = [Chord(chord) for chord in chords]
    create_midi(chords,instrument)
    play_midi()

if __name__ == "__main__":
    main()



    
