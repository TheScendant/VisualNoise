# VisualNoise

## An Audio Visualizer for Python

Plays a wave file and creates an ascii graph of the frequency distribution in real time using a 
Fast Fourier Transform and binning by every fourth note from c2 to c5.

### Dependencies:  
  * Numpy  
  * Scipy  
  * Pyaudio  
  * Argparse

### Running:
    python VisualNoise [filename] [--hor]
    filename: The name of the file to play. Defaults to Crystallize.wav
    --hor:    Displays Visualizer in horizontally instead or vertically  
