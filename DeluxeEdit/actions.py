from urllib.parse import quote, unquote
from enum import Enum

class Actions:
    class ActionId(Enum): URLENCODE = 1; URLDENCODE= 2;
      
    def mapEnum(self,indata):
         map=self.ActionId.URLENCODE 

    def run(self, indata,actionId): return self.ecodeUrl(self,indata)
    def run(self, indata,actionId):return self.decodeUrl(self,indata)

    def ecodeUrl(self,indata):
        result=quote(indata)
        return result
    
    def decodeUrl(self,indata):
        result=unquote(indata)
        return result