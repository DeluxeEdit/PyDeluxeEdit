from ctypes import sizeof
from genericpath import isfile
import os
import chardet
from util import * 
class Api:
 
    def loadFile(path,hexView=False):
        ReadBufferSizeBytes = 32 * 1024
 
        with open(path,"r") as myFile:
            detector = chardet.universaldetector.UniversalDetector()
            
        if os.path.isfile(path):
            fileSize=os.path.getsize(path)
            data=detector.feed(ReadBufferSizeBytes)
            if hexView:
                result +=Util.BytesToHex(data)

             # for x in range(0, fileSize /ReadBufferSizeBytes):
                
    #       

