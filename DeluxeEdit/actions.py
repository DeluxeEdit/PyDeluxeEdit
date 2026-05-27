from urllib.parse import quote, unquote
from enum import Enum
from zipfile import ZIP_BZIP2

class Actions:
    
    class ActionId(Enum): URLENCODE = 1; URLDENCODE= 2;
      

   
    def mapEnum(self,indata,actionId):
        self.mappedFunc=None
        if actionId is self.ActionId.URLENCODE:
            self.mappedFunc=self.ecodeUrl
        elif actionId is self.ActionId.URLDENCODE:
            self.mappedFunc=self.decodeUrl
          
        return self.mappedFunc

    def runMapped(self,indata,actionId):
      mapped=  self.mapEnum(indata,actionId)
      if (mapped): return mapped(indata)
     
      def ecodeUrl(self,indata):
        result=quote(indata)
        return result
    
    def decodeUrl(self,indata):
        result=unquote(indata)
        return result