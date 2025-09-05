import os
from ..models import FileInfo
class Util: 
    @staticmethod
    def getFiles(path, name):
        result=[]

        for root, dir, files in os.walk(path):
            if name in files:
                item=FileInfo()
                item.path=os.path.join(root, name)
                item.modified=os.path.getmtime(  item.path )
                result.append(item)


        return  result 

