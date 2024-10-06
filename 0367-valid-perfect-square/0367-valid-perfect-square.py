class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # calc sqaure root
        root = math.sqrt(num)
        
        # return true if ceiling and int cast at the same (AKA whole number)
        return math.ceil(root) == int(root) 