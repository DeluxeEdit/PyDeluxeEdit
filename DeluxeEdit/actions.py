from urllib.parse import quote, unquote

class Actions:
    def ecodeUrl(self,indata):
        result=quote(indata)
        return result
    
    def decodeUrl(self,indata):
      result=unquote(indata)
      return result