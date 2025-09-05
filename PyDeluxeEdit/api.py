from ctypes import sizeof
from genericpath import isfile
import os

class Api:
    def loadFile(path,hexView=False):
        ReadBufferSizeBytes = 32 * 1024
 
        file = open(path, "r")

        if os.path.isfile(path):
            fileSize=os.path.getsize(path)
            for x in range(0, fileSize /ReadBufferSizeBytes):
                 data = file.read(ReadBufferSizeBytes)
                 
    #"{:02X}"        

