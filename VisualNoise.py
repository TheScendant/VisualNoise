"""
Author: Hayden M Nier
Date: May 10, 2017
"""


import sys,wave,struct,math,os,time
#import cv2
import numpy as np
from scipy.fftpack import fft
import pyaudio
from ascii_graph import Pyasciigraph


def main():
    try:
        filename = sys.argv[1]
    except:
        print "Include custom song as command line arg if desired."
        print "Defaulting to Crystallize.wav"
        filename = "Crystallize.wav"

    wf = wave.open(filename, 'rb')

    p = pyaudio.PyAudio()
    pFormat = p.get_format_from_width(wf.getsampwidth())
    pSS = p.get_sample_size(pFormat)
    pMax = float(2.0 ** (pSS * 8 - 1))
    pChannels = wf.getnchannels()
    pRate = wf.getframerate()                           #Sampling Rate --- 44.1 kHz
    stream = p.open(format = pFormat,channels=pChannels,rate=pRate,output=True)

    frameCount = 2048
    fSpace = pRate/frameCount
    #bins = makeBins(pRate);
    data = wf.readframes(frameCount)                    #start frame

    
    #c2,f2,c3,f3,c4,f4,c5
    cs = [65.4,87.3,130.8,174.6,261.6,349,523.2]


#    cmax = 0
    #for hax in range(3):
    barNum = 0
    while data != '':
        array = np.array(struct.unpack("%dh" % (pChannels*frameCount),data)) /pMax   #normalize 1 to -1

        left = array[::2]
        leftFFT = np.fft.fft(left,frameCount)
        lPower = [math.sqrt( (x.real **2) + x.imag **2) for x in leftFFT]
        
        right = array[1::2]
        rightFFT = np.fft.fft(right,frameCount)
        rPower = [math.sqrt( (x.real **2) + x.imag **2) for x in rightFFT]
        #print lPower    

        bars = calcBar(lPower,rPower,cs,fSpace)
        if not sum(bars) == 0:
            bars = [(1,x) for x in bars]
            #bars.append([1,1])
            os.system('clear')
            graph = Pyasciigraph()
            line = graph.graph('Visualizer',bars)
            for x in range(len(line)):
                print (line[x])
            print "###############################################################################"
        #fSpace = pRate/float(len(lPower))               #Frequency Spacing.
        #print fSpace

        stream.write(data)                              #play
        data = wf.readframes(frameCount)                #next frame

    stream.stop_stream()
    stream.close()
    p.terminate()


def calcBar(lPower,rPower,cs,fSpace):
    bars = [0.0 for x in range(len(cs))]
    sizes = [0 for x in range(len(cs))]
    currBar = 0
    for x in range(1,(len(lPower) /2)+1):
        if (x*fSpace) < cs[currBar]:
            bars[currBar] +=((lPower[x] + rPower[x])/2.0)
            sizes[currBar] +=1
        elif (x*fSpace) > cs[-1]:
            break
        else:
            currBar +=1
            bars[currBar] +=((lPower[x] + rPower[x])/2.0)
            sizes[currBar]+=1
    for x in range(len(bars)):
        if not sizes[x]  == 0:
            bars[x] = bars[x] / float(sizes[x])
    return bars    
main()
