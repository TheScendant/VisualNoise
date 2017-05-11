"""
Author: Hayden M Nier
Date: 5.11.17

Prints a histogram of the given values.
"""

def printHist(bars):
    gmax = 600
    gheight = 36                                    #height of screen, should auto generate somehow
    lineVal = gmax / float(gheight)
    graph = [ "" for x in range(gheight)]           #graph goes top to bottom. graph[-1] is at bottom of screen

    for x in range(len(graph)):
        out = "\t\t"
        for b in bars:
            if b >  ( (gheight - x) * lineVal) :
                out += unichr(11035)
                out += unichr(11035)
            else:
                out += "  "
            out += "\t\t"
        graph[x] = out

    for line in graph:
        print line
