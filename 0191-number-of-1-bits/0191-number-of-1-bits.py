class Solution:
    def hammingWeight(self, n: int) -> int:
        
        s = str(bin(n))[2:]
        
        nums = [int(char) for char in s]
        
        total = 0
        for num in nums:
            total += num
        
        return total