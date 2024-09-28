import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
                
        # Case: empty string --> FALSE
        if s == "":
            return True;
        
        # remove all non-alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        # convert all letters to lowercase
        s = s.lower()
        
        
        length = len(s)

        # check each opposite positon for match, if yes --> FALSE
        for i in range(math.floor(length/2)):
            if s[i] != s[length - (i+1)]:
                return False
        
        # if we reach here, no mismatches --> TRUE
        return True