import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Case: negative number --> FALSE
        if x < 0:
            return False;
        
        # convert int into string
        num = str(x)
        length = len(num)

        # check each opposite positon for match, if yes --> FALSE
        for i in range(math.floor(length/2)):
            if num[i] != num[length - (i+1)]:
                return False
        
        # if we reach here, no mismatches --> TRUE
        return True