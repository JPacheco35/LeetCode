class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Case: empty list --> LCP = ""
        if len(strs) == 0:
            return ""   
        
        # Case: only 1 string in list --> LCP is that string
        if len(strs) == 1:
            return strs[0]
        
        # Case: there is an empty string in list --> LCP = ""
        for str in strs:
            if str == "":
                return ""
        
        # start with first char
        prefix = strs[0][0]
        curLength = 1
        
        
        while True:
            
            # check each string of a prefix mismatch --> return previous loop's prefix
            for str in strs:
                if str[:curLength] != prefix:
                    return prefix[:curLength-1]
                
            # prefix is the entire first string --> end here, no more characters to pull from
            if prefix == strs[0]:
                return prefix
            
            # add next charcter to the prefix
            prefix += strs[0][curLength]

            # res = prefix
            curLength += 1
