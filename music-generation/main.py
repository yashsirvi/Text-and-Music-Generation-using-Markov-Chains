from play_song import *

def main():
    chords = ["C", "G", "Am", "F"]
    chords = [Chord(chord) for chord in chords]
    create_midi(chords)
    play_midi()

if __name__ == "__main__":
    main()



    
