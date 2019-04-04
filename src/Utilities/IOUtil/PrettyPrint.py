'''
Created on Oct 21, 2009

@author: David McGinnis
'''

import math

def printComplex(Result):
    for elem in Result:
        print '%2.4f+%2.4fj' % (elem.real, elem.imag) 
   
def printResults(Result):
    for elem in Result:
        print '%2.4f' % (elem)
        
def printMostPowerful(FFTed):
    topIndicies = []
    topPowers = []
    
    for i in range(0, 10):
        currIndex = 0
        topIndicies = topIndicies + [0]
        topPowers = topPowers + [0]
        for result in FFTed:
            if (topPowers[i] < result):
                topIndicies[i] = currIndex
                topPowers[i] = result
            currIndex += 1
        topPowers[i] = FFTed[topIndicies[i]]
        FFTed = FFTed[:topIndicies[i]] + [0] + FFTed[(topIndicies[i]+1):]
    currIndex = 0
    for i in topIndicies:
        print "Found max at %4d with power %5.5f" % (i, topPowers[currIndex])
        currIndex += 1