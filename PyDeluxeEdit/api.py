from ctypes import sizeof
from genericpath import isfile
import os
import chardet
from util import * 
class Api:
    ReadBufferSizeBytes = 32 * 1024
    
    def saveFile(filePath, text):
              with open(filePath, 'w') as f:
                f.write(text)
      

    def loadFile(filePath,hexView=False):
        result=[]
        with open(filePath,"r") as myFile:
            if os.path.isfile(filePath):
                fileSize=os.path.getsize(filePath)
                for x in range(0, fileSize /Api.ReadBufferSizeBytes):
                    if hexView:
                        data=myFile.read(Api.ReadBufferSizeBytes)
                        result.append(Util.BytesToHexStrings(data))
                    else:
                        detector = chardet.universaldetector.UniversalDetector()
                        detector.feed(Api.ReadBufferSizeBytes)
                        lines=detector.done()
                        result.append(lines  )
                        detector.close()
                    return result
