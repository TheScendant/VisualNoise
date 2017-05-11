"""
Author: Hayden M Nier
Date: 5.11.17

Prints a histogram of the given values.
"""

def printHist(bars):
    gmax = 600
    gWidth = 140
    colVal = gmax / float(gWidth)
    print "\n"


    for bar in bars:
        out= ""
        for x in range(gWidth):
            if (x*colVal) <= bar:
                out+="*"
            else:
                break
        print out
        print out
        print out
        print "\n"


