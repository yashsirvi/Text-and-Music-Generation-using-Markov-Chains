from play_song import *

def main():
    chords = ["C", "G", "Am", "F"]
    chords = [Chord(chord) for chord in chords]
    create_midi(chords)

if __name__ == "__main__":
    main()



    
