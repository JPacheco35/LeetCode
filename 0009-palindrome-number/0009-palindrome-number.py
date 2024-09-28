import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Case: negative number --> FALSE
        if x < 0:
            return False;
        
        # convert int into string
        num = str(x)
        length = len(num)
        
        # Case: single digit --> TRUE
        # if length == 1:
        #     return True
        
#         if length == 2:
#             return num[0] == num[1]
        
        # if length == 3:
        #     return num[0] == num[2]

        
        for i in range(math.floor(length/2)):
            if num[i] != num[length - (i+1)]:
                return False
        
        return True