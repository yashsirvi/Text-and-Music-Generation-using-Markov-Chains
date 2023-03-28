# from utils import load_files
import os
import pickle
import pprint
import process_mc

curr_dir = os.path.dirname(os.path.realpath(__file__))

def get_probabilities(chord_blocks):
    probabilities = dict((chord, dict((next_chord, chord_blocks[chord].count(next_chord) / len(chord_blocks[chord])) for next_chord in chord_blocks[chord])) for chord in chord_blocks)
    # remove chords that only appear once
    probabilities = dict((chord, probabilities[chord]) for chord in probabilities if len(probabilities[chord]) > 1)
    return probabilities

def main():
    chord_blocks=process_mc.get_chord_blocks()
    probabilities = get_probabilities(chord_blocks)
    sorted_probabilities = dict((chord, sorted(probabilities[chord].items(), key=lambda x: x[1], reverse=True)) for chord in probabilities)
    # flatten the dictionary
    flattened = tuple((chord, next_chord, probability) for chord in sorted_probabilities for next_chord, probability in sorted_probabilities[chord])
    # sort by probability
    flattened = sorted(flattened, key=lambda x: x[2], reverse=True)
    pp = pprint.PrettyPrinter(depth=2)
    pp.pprint(flattened[:10])

if __name__ == "__main__":
    main()