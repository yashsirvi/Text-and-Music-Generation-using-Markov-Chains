import os
import re
import random


def gen_text(data, block_type="word", block_size=3, words=20, characters=100):
    """
    data is input folder containing text files
    block_type is either "word" or "ngram"
    block_size is the number of words in each ngram
    words is the number of words to generate
    characters is the number of characters to generate
    """
    blocks = get_blocks(data, block_type, block_size)
    if block_type == "word":
        return gen_word_blocks(blocks, words)
    elif block_type == "ngram":
        return gen_ngram_text(blocks, characters)


def get_blocks(data, block_type="word", block_size=3):
    """
    data is input folder containing text files
    block_type is either "word" or "ngram"
    """
    if block_type == "word":
        return get_words(data)
    elif block_type == "ngram":
        return get_ngrams(data, block_size)
    else:
        raise ValueError("block_type must be either 'word' or 'ngram'")


def get_words(data):
    """
    data is input folder containing text files
    """
    blocks = {} 
    for file in os.listdir(data):
        with open(os.path.join(data, file), "r") as f:
            line = f.read().replace("\n", " ")
            line = re.sub(r"[\[\]\"\'()]", "", line)
            words = re.findall(r"[\w]+|[^\s\w]", line)
            # words = list(filter(None, words))
            words = list(filter(lambda x: x != " ", words))
            words[0] = words[0].lower()
            for i in range(len(words) - 1):
                words[i + 1] = words[i + 1].lower()
                if words[i] not in blocks:
                    blocks[words[i]] = [words[i + 1]]
                else:
                    blocks[words[i]].append(words[i + 1])
    return blocks

def get_ngrams(data, block_size):
    """
    data is input folder containing text files
    block_size is the number of words in each ngram   
    """
    blocks = {} 
    for file in os.listdir(data):
        with open(os.path.join(data, file), "r") as f:
            line = f.read().replace("\n", " ")
            line = re.sub(r"[\[\]\"\'()]", "", line)
            # split the line into substrings of length block_size
            words = [line[i:i+block_size] for i in range(0, len(line) - block_size + 1)]
            words[0] = words[0].lower()
            for i in range(len(words) - 1):
                words[i + 1] = words[i + 1].lower()
                if words[i] not in blocks:
                    blocks[words[i]] = [words[i + 1][-1]]
                else:
                    blocks[words[i]].append(words[i + 1][-1])
    return blocks

def gen_word_blocks(blocks, size=10):
    """
    blocks is a dictionary of blocks
    size is the number of words to generate
    """
    word = random.choice(list(blocks.keys()))
    text = [word]
    for i in range(size):
        word = random.choice(blocks[word])
        text.append(word)
    return human_readable_join(text)


def human_readable_join(words):
    """
    words is a list of words
    """
    output = ""
    for word in words:
        if word in [".", "!", "?", ",", ";", ":"]:
            output += word
        else:
            output += " " + word
    return output.strip()

def gen_ngram_text(blocks, size=3):
    """
    blocks is a dictionary where keys are ngrams of size 'size' and values are lists of characters
    """
    word = random.choice(list(blocks.keys()))
    text = [word]
    curr_ngram = word
    for i in range(size):
        if curr_ngram not in blocks:
            curr_ngram = random.choice(list(blocks.keys()))
        char = random.choice(blocks[curr_ngram])
        text.append(char)
        curr_ngram = curr_ngram[1:] + char
    return "".join(text)