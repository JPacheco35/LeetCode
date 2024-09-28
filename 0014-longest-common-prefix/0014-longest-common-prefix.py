class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        for str in strs:
            if str == "":
                return ""
        
        res = ""
        prefix = ""
        # print(prefix)
        curLength = 1
        while True:
            # print("prefix = " + prefix)
            if prefix == strs[0]:
                return prefix
            
            prefix += strs[0][curLength-1]
            for str in strs:
                if str[:curLength] != prefix:
                    return res
            res = prefix
            curLength += 1
            