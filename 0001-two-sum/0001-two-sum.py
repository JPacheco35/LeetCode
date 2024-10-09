class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # get length of array
        length = len(nums)
        
        # loop thorugh each possible pairing --> o(n^2)
        for i in range(length):
            for j in range(length):
                
                # can't add same num twice 
                if i == j:
                    continue
                    
                # if two num add to target, return indices
                if nums[i] + nums[j] == target:
                    return [i,j]
                
        # we should never reach here
        return [-1,0]