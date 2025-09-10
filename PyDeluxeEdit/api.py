from ctypes import sizeof
from genericpath import isfile
import os
import chardet
from util import * 
class Api:
    ReadBufferSizeBytes = 32 * 1024
    
    def saveFile(path, text):
              with open(path, 'w') as f:
                f.write(text)
      

    def loadFile(path,hexView=False):
        result=[]
 
        with open(path,"r") as myFile:
             if not hexView:
                
                  
              if os.path.isfile(path):
                fileSize=os.path.getsize(path)
                for x in range(0, fileSize /Api.ReadBufferSizeBytes):
           
     #     detector.feed(ReadBufferSizeBytes)
                    if hexView:
                        data=myFile.read(Api.ReadBufferSizeBytes)
                        result.append.BytesToHexString(data)
                    else:
                        detector = chardet.universaldetector.UniversalDetector()
                        detector.feed(Api.ReadBufferSizeBytes)
                        lines=detector.done()
                        result.append(lines  )
                        detector.close()
                    
                #       

