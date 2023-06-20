# Markov Chain Text and Music Generator

MA41017:STOCHASTIC PROCESSES Team Project

This project uses Markov chains to generate text and music based on input data. The model creates a Markov chain with words or chords as states, and the transition probabilities are calculated empirically using the input data. The model then generates text and music by sampling from the Markov chain.

## Dependencies
Install dependencies using `pip install -r requirements.txt`.

## Text Generation

### Usage 
- Put your input data in form of .txt files in the `input` folder.
- Edit `main.py` to specify the input files and the number of words to generate.
- Run `python main.py` to generate text

### Input data format
The input data for the text generation should be a text file containing words or sentences separated by a newline. 

## Music Generation

### Usage
- Set up Spotify API using the instructions [here](https://developer.spotify.com/documentation/web-api).
- Note your Client ID and Client Secret.
- Create a file `config.py` in the `music-generation` directory and add the following lines to it:
```py
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
```
- To generate the required data, run the script `gen_data.sh` using `bash gen_data.sh`.
- Finally, run `python main.py` to generate music.
- `main.py` has certain arguments that can be passed to it, which can be seen by running `python main.py --help`.



## Some Results
```
1. chandra shekhar. morgan freeman, and biebers believe that steven spielberg and forces engaged in 1664, loss of country singer harry assumes in february 2018

2. joke, but its actually beggin for $8/month.   depending and thinks that twitter and all their emissivity is a 3 or 2.

3. D, A, Bm, E, G, Am, C, Em, C, A#9, Bb

4. F, C, D, E, F#m, D, G, Bm, E, B, Eb
```

## Limitations

- The Markov chain model used in this project has limitations in generating coherent and grammatically correct natural language texts. The generated text may contain grammatical errors and lack coherence. Similarly, the generated music may not capture the full complexity of the input data.
- The scraping of chords for music progression is currently done synchronously, which is slow. This can be improved by making the code asynchronous.