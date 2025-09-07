from ctypes import sizeof
from genericpath import isfile
import os
import chardet
from util import * 
class Api:
 
    def loadFile(path,hexView=False):
        ReadBufferSizeBytes = 32 * 1024
 
        with open(path,"r") as myFile:
             if not hexView:
                
            
              if os.path.isfile(path):
                fileSize=os.path.getsize(path)
                data=myFile.read(ReadBufferSizeBytes)
                #     detector.feed(ReadBufferSizeBytes)
                if hexView:
                    result +=Util.BytesToHex(data)
                else:
                    detector = chardet.universaldetector.UniversalDetector()
                    # for x in range(0, fileSize /ReadBufferSizeBytes):
                
                #       

