from utils import *
import pickle

def load_files(type = "tweets", block_size = 7):
    afile = open(f"{type}_word_blocks.pkl", "rb")
    word_blocks = pickle.load(afile)
    afile.close()
    afile = open(f"{type}_ngram_{block_size}_blocks.pkl", "rb")
    ngram_blocks = pickle.load(afile)
    afile.close()
    return word_blocks, ngram_blocks


def save_files(data, type="tweets", block_size = 7):
    word_blocks = get_words(data)
    ngram_blocks = get_ngrams(data, block_size)
    afile = open(f"{type}_word_blocks.pkl", "wb")
    pickle.dump(word_blocks, afile)
    afile.close()
    afile = open(f"{type}_ngram_{block_size}_blocks.pkl", "wb")
    pickle.dump(ngram_blocks, afile)
    afile.close()

def main():
    data = "data"
    block_type1 = "word"
    block_type2 = "ngram"
    block_size = 7
    words = 30
    characters = 300
    # save_files(data)
    word_blocks, ngram_blocks = load_files()
    output_word = gen_word_blocks(word_blocks, words)
    output_ngram = gen_ngram_text(ngram_blocks, characters)
    print("word blocks: \n\t" + output_word)
    print()
    print("ngrams: \n\t"+ output_ngram)

if __name__ == "__main__":
    main()