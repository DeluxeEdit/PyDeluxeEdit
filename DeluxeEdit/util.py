import os


class Util:
    @staticmethod
    def ExecuteShell(self,cmd):
        os.system(cmd)
  

    @staticmethod
    def ByteToHexString(self,b):
        result=str.format(b, " {:02X} " ) 
        return result

    @staticmethod
    def BytesToHexStrings(self,a):
        result=[]
        for b in a:
            result.append(Util.ByteToHexString(b)  )
            
        return result
    