'''
Created on Oct 22, 2009

@author: David McGinnis
'''

from Utilities.SigUtil import FFT
from Utilities.SigUtil import SignalUtilities
from Utilities.IOUtil import PrettyPrint
from Utilities.IOUtil import FileIO

def testAmplitude():
    input = open("testdata.csv", 'r')
    data = input.readline().split(',')
    print "Starting..."
    PrettyPrint.getMostPowerful(FFT.DFT(data))
    print "Finished."
    
def testDFT():
    input = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1]
    results = FFT.DFT(input)
    i = 0
    for result in results:
        print "y%1d = %2.4f" % (i, result)
        i += 1
        
def testParsing():
    data = FileIO.OReillyParse("E:/Code/Python/Diginome/440A.wav")
    print "First five results: "
    for i in range(0, 6):
        print data[i]
        
testParsing()