from utils import load_files
import os
import pickle
import pprint

curr_dir = os.path.dirname(os.path.realpath(__file__))

def get_probabilities(word_blocks):
    probabilities = dict((word, dict((next_word, word_blocks[word].count(next_word) / len(word_blocks[word])) for next_word in word_blocks[word])) for word in word_blocks)
    # remove words that only appear once
    probabilities = dict((word, probabilities[word]) for word in probabilities if len(probabilities[word]) > 1)
    return probabilities

def save_probabilities(probabilities, type="tweets"):
    afile = open(f"{curr_dir}/saved_data/probabilities_{type}.pkl", "wb")
    pickle.dump(probabilities, afile)
    afile.close()

def load_probabilities(type="tweets"):
    afile = open(f"{curr_dir}/saved_data/probabilities_{type}.pkl", "rb")
    probabilities = pickle.load(afile)
    afile.close()
    return probabilities

def main():
    word_blocks, ngram_blocks = load_files()
    # probabilities = get_probabilities(word_blocks)
    # save_probabilities(probabilities)
    probabilities = load_probabilities()
    sorted_probabilities = dict((word, sorted(probabilities[word].items(), key=lambda x: x[1], reverse=True)) for word in probabilities)
    # flatten the dictionary
    flattened = tuple((word, next_word, probability) for word in sorted_probabilities for next_word, probability in sorted_probabilities[word])
    # sort by probability
    flattened = sorted(flattened, key=lambda x: x[2], reverse=True)
    pp = pprint.PrettyPrinter(depth=2)
    pp.pprint(flattened[:10])

if __name__ == "__main__":
    main()