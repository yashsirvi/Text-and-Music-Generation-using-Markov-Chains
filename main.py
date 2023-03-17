from utils import *

def main():
    data = "data"
    block_type1 = "word"
    block_type2 = "ngram"
    block_size = 3
    words = 20
    characters = 100
    output_word_blocks = gen_text(data, block_type1, block_size, words, characters)
    output_ngram_blocks = gen_text(data, block_type2, block_size, words, characters)
    print(output_word_blocks)
    print()
    print(output_ngram_blocks)

if __name__ == "__main__":
    main()