import pretty_midi
import pygame
import os
from pychord import *

curr_dir = os.path.dirname(os.path.realpath(__file__))
chord_progression_file = f"{curr_dir}/data/chord_progression.mid"

def create_midi(chords, instrument, filename=chord_progression_file):
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program(instrument)
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)
    midi_data.write(filename)

def play_midi(filename=chord_progression_file):
    # play it in a loop
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


        

