import sys,wave,struct,math,os,time
#import cv2
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
    pMax = float(2.0 ** (p.get_sample_size(pFormat) * 8 - 1))
    pChannels = wf.getnchannels()
    pRate = wf.getframerate()                           #Sampling Rate --- 44,1000
    stream = p.open(format = pFormat,channels=pChannels,rate=pRate,output=True)

    frameCount = 512

    data = wf.readframes(frameCount)                    #start frame
    while data != '':
        array = np.array(struct.unpack("%dh" % (pChannels*frameCount),data))/pMax   #normalize 1 to -1

        left = array[::2]
        leftFFT = np.fft.fft(left,frameCount)
        lPower = [math.sqrt( (x.real **2) + x.imag **2) for x in leftFFT]
        
        right = array[1::2]
        rightFFT = np.fft.fft(right,frameCount)
        rPower = [math.sqrt( (x.real **2) + x.imag **2) for x in rightFFT]
        
        #fSpace = pRate/float(len(lPower))               #Frequency Spacing. len(lPower)
        
        #graphPowerArrays


        stream.write(data)                              #play
        data = wf.readframes(frameCount)                #next frame

    stream.stop_stream()
    stream.close()
    p.terminate()

main()
