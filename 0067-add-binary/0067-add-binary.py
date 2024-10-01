class Solution:
    def addBinary(self, a: str, b: str) -> str:
                
        # read in each string as binary, convert to int
        a = int(a, base=2)
        b = int(b, base=2)
        
        # add both ints, return as string without 1st 2 chars 
        # ie. "0b100"--> "100"
        return str(bin(a+b))[2:]