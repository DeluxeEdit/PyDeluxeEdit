from unittest import result


class Util:
    @staticmethod
    def ExecuteCommand(cmd):
        v=""    

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
    