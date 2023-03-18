from utils import *

def main():
    data = "data"
    block_type1 = "word"
    block_type2 = "ngram"
    block_size = 10
    words = 30
    characters = 300
    output_word_blocks = gen_text(data, block_type1, block_size, words, characters)
    output_ngram_blocks = gen_text(data, block_type2, block_size, words, characters)
    print("word blocks: \n\t" + output_word_blocks)
    print()
    print("ngrams: \n\t"+ output_ngram_blocks)

if __name__ == "__main__":
    main()