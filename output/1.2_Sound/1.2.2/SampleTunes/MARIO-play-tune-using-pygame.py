import pygame
import time
import numpy as np

# Initialize Pygame mixer
pygame.mixer.init()

# Define the frequencies of the notes
note_freqs = {
    'C3': 130.81, 'C#3': 138.59, 'D3': 146.83, 'Eb3': 155.56, 'E3': 164.81,
    'F3': 174.61, 'F#3': 185.00, 'G3': 196.00, 'G#3': 207.65, 'A3': 220.00,
    'Bb3': 233.08, 'B3': 246.94, 'C4': 261.63, 'C#4': 277.18, 'D4': 293.66,
    'Eb4': 311.13, 'E4': 329.63, 'F4': 349.23, 'F#4': 369.99, 'G4': 392.00,
    'G#4': 415.30, 'A4': 440.00, 'Bb4': 466.16, 'B4': 493.88, 'C5': 523.25,
    'C#5': 554.37, 'D5': 587.33, 'Eb5': 622.25, 'E5': 659.25, 'F5': 698.46,
    'F#5': 739.99, 'G5': 783.99, 'G#5': 830.61, 'A5': 880.00, 'Bb5': 932.33,
    'B5': 987.77, 'C6': 1046.50
}


# Function to play a single note
def play_tone(frequency, duration):
    if frequency:
        sample_rate = 44100
        n_samples = int(round(duration * sample_rate))
        t = np.linspace(0, duration, n_samples, False)
        wave = 4096 * np.sin(2 * np.pi * frequency * t)
        stereo_wave = np.column_stack((wave, wave))
        sound = pygame.sndarray.make_sound(stereo_wave.astype(np.int16))
        sound.play(-1)
        time.sleep(duration)
        sound.stop()
    else:
        time.sleep(duration)

# Super Mario theme tune
tune = [
    ('E4', 0.125), ('E4', 0.125), ('E4', 0.125), (None, 0.125), ('C4', 0.125), ('E4', 0.125), ('G4', 0.125), (None, 0.375),
    ('G3', 0.125), (None, 0.375), ('C4', 0.125), (None, 0.25), ('G3', 0.125), (None, 0.25), ('E3', 0.125), (None, 0.125),
    ('A3', 0.125), (None, 0.125), ('B3', 0.125), (None, 0.125), ('Bb3', 0.125), ('A3', 0.125), (None, 0.125), ('G3', 0.125),
    ('E4', 0.125), ('G4', 0.125), ('A4', 0.125), (None, 0.125), ('F4', 0.125), ('G4', 0.125), (None, 0.125), ('E4', 0.125),
    ('C4', 0.125), ('D4', 0.125), ('B3', 0.125), (None, 0.125)
]

# Play the tune
for note, duration in tune:
    if note:
        frequency = note_freqs[note]
    else:
        frequency = None
    play_tone(frequency, duration)

# Quit Pygame mixer
pygame.mixer.quit()
