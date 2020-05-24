# VisualNoise

## An Audio Visualizer for Python

Plays a wave file and creates an ascii graph of the frequency distribution in real time using a 
Fast Fourier Transform and binning by every fourth note from c2 to c5.

### Dependencies:  
  * Numpy  
  * Scipy  
  * Pyaudio  
  * Argparse

### Setup (As of May 2020):
  You may need to:
  ```
  > sudo apt-get install python3-pyaudio &&
    pip3 install pyaudio
  ```

### Running:
    python VisualNoise [filename] [--hor]
    filename: The name of the file to play. Defaults to EyesOnFire.wav
    --hor:    Displays Visualizer in horizontally instead or vertically  
