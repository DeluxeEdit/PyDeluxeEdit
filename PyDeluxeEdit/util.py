import os


class Util:
    @staticmethod
    def ExecuteShell(cmd):
        os.system(cmd)
  

    @staticmethod
    def ByteToHexString(b):
        result=str.format(b, " {:02X} " ) 
        return result

    @staticmethod
    def BytesToHexStrings(a):
        result=[]
        for b in a:
            result.append(Util.ByteToHexString(b)  )
            
        return result
    