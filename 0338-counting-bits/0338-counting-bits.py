class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0] * (n+1)
        
        
        # find number of 1 bits in each number from 0-n
        for i in range(n+1):
            
            count = 0
            j = i

            # while i > 0
            while j > 0:

                # Case: rightmost bit (LSB) is 1
                count += j&1

                # shift n to the right 1 bit to check next bit
                j = j >> 1
              
            # store # of 1 bits
            res[i] = count
            

        return res