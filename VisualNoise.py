import sys,wave,struct
import cv2
import numpy as np
from scipy.fftpack import fft
import pyaudio


def main():
    try:
        filename = sys.argv[1]
    except:
        print "Defaulting to Crystallize.wav"
        filename = "Crystallize.wav"

    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()
    pFormat = p.get_format_from_width(wf.getsampwidth())
    pMax = (2.0 ** (p.get_sample_size(pFormat) * 8 - 1))
    pChannels = wf.getnchannels()
    pRate = wf.getframerate()
    stream = p.open(format = pFormat,channels=pChannels,rate=pRate,output=True)

    frameCount = 512

    data = wf.readframes(frameCount)
    while data != '':
        array = np.array(struct.unpack("%dh" % (pChannels*frameCount),data))/pMax

        stream.write(data)
        data = wf.readframes(frameCount)

    stream.stop_stream()
    stream.close()
    p.terminate()

main()
