'''
Created on Oct 22, 2009

@author: David McGinnis
'''

from Utilities.SigUtil import FFT
from Utilities.SigUtil import SignalUtilities
from Utilities.IOUtil import PrettyPrint
from Utilities.IOUtil import FileIO
import datetime

def FileTest():
    print "Starting..."
    StartTime = datetime.datetime.now()
    print "Parsing Wav File..."
    data = FileIO.ParseWav("E:/Code/Python/Diginome/440A.wav")
    ParseTime = datetime.datetime.now()
    print "Done. Took %5d microseconds." % (ParseTime - StartTime).microseconds
    print "FFTing..."
    FFT.DFT(data)
    FFTTime = datetime.datetime.now()
    print "Done FFTing data. Took %5d seconds." % (FFTTime - ParseTime).seconds
    print "Finding most powerful..."
    PrettyPrint.printMostPowerful(data[40:600])
    PrintingTime = datetime.datetime.now()
    print "Done. Took %5d microseconds." % (PrintingTime - FFTTime).microseconds
    print "Exporting Data..."
    FileIO.ExportToCSV(data)
    DoneTime = datetime.datetime.now()
    print "Done. Took %5d microseconds." % (DoneTime - PrintingTime).microseconds
    EndTime = datetime.datetime.now()
    delta = EndTime - StartTime
    print "Finished. Completed in %5d seconds." % (delta.seconds)
    

def DFTTest():
    input = open("testdata.csv", 'r')
    data = input.readline().split(',')
    print "Starting..."
    StartTime = datetime.datetime.now()
    PrettyPrint.printResults(FFT.DFT(data))
    EndTime = datetime.datetime.now()
    delta = EndTime - StartTime
    print "Finished. Completed in %5d microseconds." % (delta.microseconds)
    
FileTest()