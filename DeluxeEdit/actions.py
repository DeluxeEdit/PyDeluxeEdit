from unittest import result
from urllib.parse import quote, unquote
from enum import Enum

class Actions:
    
    class ActionItem:
        name=""
        mapped=None

             
   
  
    def runMapped(self,indata,actionId):
      mapped=  self.mapEnum(indata,actionId)
      if (mapped): return mapped(indata)
     

    @staticmethod
    def encodeUrl(self,indata):
        result=quote(indata)
        return result

    @staticmethod
    def decodeUrl(self,indata):
        result=unquote(indata)
        return result

    def getActions(self):
        result=[]
        itemEnc=self.ActionItem()
        itemEnc.name="EncodeUrl"
#        itemEnc.mapped=self.encodeUrl
        result.append(itemEnc)
        itemDec=self.ActionItem()
        itemDec.name="DecodeUrl"
  #      itemDec.mapped=self.decodeUrl
        result.append(itemDec)
        return result        