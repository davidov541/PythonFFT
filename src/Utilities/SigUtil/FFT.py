'''
Created on Oct 2, 2009

@author: David McGinnis
'''

import math
from Utilities.IOUtil import PrettyPrint

# Takes A, and converts all elements using the getYk function into
# the term for the Discrete Fourier Transform.
def DFT(Sig):
    returnable = []
    n = 0
    for elem in Sig:
        yk = getYk(Sig, n)
        #realpart = round(yk.real, 3)
        #imagpart = 1j * round(yk.imag, 3)
        realpart = yk.real
        imagpart = yk.imag * 1j
        returnable = returnable + [abs(realpart + imagpart)]
        n += 1
    return returnable

# Outputs the yk value for the given k, using A as the set of data points.
# Uses the DFT algorithm found in DE Book and online. Is very slow, but good
# enough for testing and preliminary application development.
def getYk(Sig, n):
    N = len(Sig)
    Yk = 0
    for k in range(0, N):
        #need to convert this to rectangular for use. Python doesn't know Euler.
        w = complex(math.cos(-2*math.pi*n*k/N), (math.sin(-2*math.pi*n*k/N)))
        currTerm = float(Sig[k])*w
        Yk += currTerm
    return Yk