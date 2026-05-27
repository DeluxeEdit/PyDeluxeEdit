from unittest import result
from urllib.parse import quote, unquote
from enum import Enum

class Actions:
    
    class ActionId(Enum): URLENCODE = 1; URLDENCODE= 2;
    
    class ActionItem:
        name=""
        action=None

             
   
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

    def getActions(self):
        result=[]
        itemEnc=self.ActionItem()
        itemEnc.name="URLENCODE"
        result.append(itemEnc)
        itemDec=self.ActionItem()
        itemDec.name="URLDENCODE"
        result.append(itemDec)
        return result        