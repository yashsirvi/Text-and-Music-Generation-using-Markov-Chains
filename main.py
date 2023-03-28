from utils import *

def main():
    data = "input"
    block_type1 = "word"
    block_type2 = "ngram"
    block_size = 20
    words = 30
    characters = 300
    # save_files(data)
    word_blocks, ngram_blocks = load_files()
    num_words = 0
    output_word = gen_word_blocks(word_blocks, words)
    output_ngram = gen_ngram_text(ngram_blocks, characters)
    print("word blocks: \n\t" + output_word)
    print()
    # print("ngrams: \n\t"+ output_ngram)

if __name__ == "__main__":
    main()