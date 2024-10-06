class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        # hash table to store values
        table = {}
        
        # loop thorugh each char in string
        for char in s:
            
            # char is already in hash table --> return that char
            if char in table:
                return char 
            
            # otherwise, add char to table
            table[str(char)] = hash(char)
            
        # we should never reach here
        return char