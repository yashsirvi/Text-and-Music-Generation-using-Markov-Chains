# Markov Chain Text and Music Generator

MA41017:STOCHASTIC PROCESSES Team Project

This project uses Markov chains to generate text and music based on input data. The model creates a Markov chain with words or chords as states, and the transition probabilities are calculated empirically using the input data. The model then generates text and music by sampling from the Markov chain.

## Dependencies
Install dependencies using `pip install -r requirements.txt`.

## Usage
- Put your input data in form of .txt files in the `input` folder.
- Edit `main.py` to specify the input files and the number of words to generate.
- Run `python main.py` to generate text

## Input data format

The input data for the text generation should be a text file containing words or sentences separated by a newline. The input data for the music generation should be a text file containing chord progressions separated by a newline.

## Some Results
```
1. chandra shekhar. morgan freeman, and biebers believe that steven spielberg and forces engaged in 1664, loss of country singer harry assumes in february 2018

2. joke, but its actually beggin for $8/month.   depending and thinks that twitter and all their emissivity is a 3 or 2.

3. D, A, Bm, E, G, Am, C, Em, C, A#9, Bb

4. F, C, D, E, F#m, D, G, Bm, E, B, Eb
```

## Limitations

The Markov chain model used in this project has limitations in generating coherent and grammatically correct natural language texts. The generated text may contain grammatical errors and lack coherence. Similarly, the generated music may not capture the full complexity of the input data.