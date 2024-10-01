class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # store # of 1 bits
        count = 0
        
        # while n > 0
        while n > 0:
            
            # Case: rightmost bit (LSB) is 1
            count += n&1
            
            # shift n to the right 1 bit to check next bit
            n = n >> 1
                
        return count