
from os import path
import os
from chardet.universaldetector import UniversalDetector
from util import * 
class Api:
    ReadBufferSizeBytes = 32 * 1024
    #ProjectUiFileName=".\\PyDeluxeEdit.ui"
    
    def saveFile(filePath, text):
              with open(filePath, 'w') as f:
                f.write(text)
      

    def loadFile(filePath,hexView=False):
        result=[]
        if not path.isfile(filePath): raise FileExistsError(filePath)
        fileSize=path.getsize(filePath)
            
        with open(filePath,"r") as myFile:
                for x in range(0, fileSize /Api.ReadBufferSizeBytes):
                    if hexView:
                        data=myFile.read(Api.ReadBufferSizeBytes)
                        result.append(Util.BytesToHexStrings(data))
                    else:
                        detector = UniversalDetector()
                        detector.feed(Api.ReadBufferSizeBytes)
                        lines=detector.done()
                        result.append(lines  )
                        detector.close()
                    return result
