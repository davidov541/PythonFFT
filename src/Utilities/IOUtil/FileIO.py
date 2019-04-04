'''
Created on Oct 21, 2009

@author: David McGinnis
'''
from Utilities.SigUtil import SignalUtilities
import struct
import wave
import sys
import array

def ParseWav(fileName):
    wavFile = open(fileName, 'rb')
    wavFile.seek(58)
    data = []
    nextString = wavFile.read(4)
    while (nextString != ""):
        data.append(struct.unpack('<f', nextString)[0])
        nextString = wavFile.read(4)
    return data

def OReillyParse(fileName):
    # open the wave file
    fp = wave.open(fileName,"rb")
    params = fp.getparams()
    sample_rate = fp.getframerate()
    total_num_samps = fp.getnframes()
    sample_width = fp.getsampwidth()
    temp = array.array('d')
    # read in the data from the file
    for i in range(total_num_samps/8 - 1):
        tempb = fp.readframes(8);
        temp2 = struct.unpack('3f', tempb)
        temp.append(temp2[0])
        temp.append(temp2[1])
        temp.append(temp2[2])
    fp.close()
    return temp
    
def ExportToCSV(data):
    fileHandle = open("data.csv", 'w')
    for datum in data:
        fileHandle.write("{0},".format(datum))
    fileHandle.close()
