from unittest import result


class Util: 
    @staticmethod
    def BytesToHex(a):
        result=[]
        for b in a:
            result.append( str.format(b, "{:02X} " ) )
            
        return result
    