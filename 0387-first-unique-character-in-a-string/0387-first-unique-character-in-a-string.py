class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        # dict to store letter frequencies 
        table = {}
        
        # loop through each char in string
        for char in s:
            
            # char already added, add one to its frequency
            if char in table:
                table[char] = table.get(char, 0) + 1
                
            # first occurence of char --> add it to dict
            else:
                table[char] = 1
        
        # loop through each char in frequnecy table
        for key,val in enumerate(table):
            
            # char only shows up once --> return that char's index
            if table.get(val,0) == 1:
                return s.find(val)
            
        # if we reach here, no unique characters --> return -1
        return -1