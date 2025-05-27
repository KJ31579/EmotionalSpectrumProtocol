#output == "random digital emotions as colors and sound :)" 

#first paste in cmd or terminal: 
#pip install pygame numpy

import random
import time
import numpy as np
import pygame
import math

# Initialize sound system
pygame.init()
pygame.mixer.init(frequency=22050, size=-16, channels=1)

# Note frequencies (C major pentatonic)
note_freqs = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'G': 392.00,
    'A': 440.00
}

# Corrected: low notes = violet, high notes = red
color_map = {
    'C': (110, 70, 175),      # Violet – lowest
    'D': (145, 162, 132),     # Olive-teal - (lowest+middle)/2
    'E': (180, 255, 90),      # Chartreuse – middle
    'G': (218, 150, 70),      # Amber - (highest+middle)/2
    'A': (255, 40, 40)        # Red – highest
}

def generate_tone(frequency, duration=0.5, sample_rate=22050):
    n_samples = int(round(duration * sample_rate))
    waveform = np.array([
        int(32767 * 0.5 * math.sin(2.0 * math.pi * frequency * t / sample_rate))
        for t in range(n_samples)
    ], dtype=np.int16)
    stereo_waveform = np.column_stack((waveform, waveform))  # make it 2D for stereo
    return pygame.sndarray.make_sound(stereo_waveform)


sequence = [random.choice(list(note_freqs.keys())) for _ in range(10)]

for note in sequence:
    freq = note_freqs[note]
    rgb = color_map[note]
    print(f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}mPlaying note: {note}\033[0m")
    sound = generate_tone(freq)
    sound.play()
    time.sleep(0.5)
    sound.stop()
    time.sleep(0.1)
