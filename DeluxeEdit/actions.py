from urllib.parse import quote, unquote

class Actions:
    def ecodeUrl(indata):
        result=quote(indata)
        return result
    
    def decodeUrl(indata):
      result=unquote(indata)
      return result