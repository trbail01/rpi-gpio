import pygame
import time
import numpy as np

### PINK PANTHER THEME ###

# Initialize Pygame mixer
pygame.mixer.init()

# Define the frequencies of the notes
note_freqs = {
    'C4': 261.63, 'C#4': 277.18, 'D4': 293.66, 'Eb4': 311.13, 'E4': 329.63,
    'F4': 349.23, 'F#4': 369.99, 'G4': 392.00, 'G#4': 415.30, 'A4': 440.00,
    'Bb4': 466.16, 'B4': 493.88
}

# Function to play a single note
def play_tone(frequency, duration):
    if frequency:
        sample_rate = 44100
        n_samples = int(round(duration * sample_rate))
        # Create a sine wave for the given frequency and duration
        t = np.linspace(0, duration, n_samples, False)
        wave = 4096 * np.sin(2 * np.pi * frequency * t)
        # Ensure the array is 2-dimensional for the stereo mixer
        stereo_wave = np.column_stack((wave, wave))
        sound = pygame.sndarray.make_sound(stereo_wave.astype(np.int16))
        sound.play(-1)
        time.sleep(duration)
        sound.stop()
    else:
        time.sleep(duration)

# The tune to play
tune = [
    ('C#4', 0.2), ('D4', 0.2), (None, 0.2),
    ('Eb4', 0.2), ('E4', 0.2), (None, 0.6),
    ('F#4', 0.2), ('G4', 0.2), (None, 0.6),
    ('Eb4', 0.2), ('E4', 0.2), (None, 0.2),
    ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
    ('C4', 0.2), ('B4', 0.2), (None, 0.2),
    ('F#4', 0.2), ('G4', 0.2), (None, 0.2),
    ('B4', 0.2), ('Bb4', 0.5), (None, 0.6),
    ('A4', 0.2), ('G4', 0.2), ('E4', 0.2),
    ('D4', 0.2), ('E4', 0.2)
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
