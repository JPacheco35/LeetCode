class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # keep track of number of ops
        total = 0 
        
        # loop thorugh each num
        for num in nums:
    
            # if number is 1 off from multiple of 3, add 1 operation to total
            if num % 3 != 0:
                total += 1
                
        # return number of operations
        return total