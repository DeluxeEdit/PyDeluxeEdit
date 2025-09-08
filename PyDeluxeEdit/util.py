from unittest import result


class Util:
    @staticmethod
    def ByteToHexString(b):
        result=str.format(b, " {:02X} " ) 
        return result

    @staticmethod
    def BytesToHexString(a):
        result=[]
        for b in a:
            result.append(Util.ByteToHexString(b)  )
            
        return result
    