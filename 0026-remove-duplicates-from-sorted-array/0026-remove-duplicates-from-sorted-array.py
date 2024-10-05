class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # store previous number (start with -999 because nums can be from -100,100)
        prev_num = -999
        i = 0
        
        # go through each item
        while i < len(nums):
            
            # if duplicate --> remove it --> check spot again
            if nums[i] == prev_num:
                nums.pop(i)
                continue
                
            # store current num for next loop
            prev_num = nums[i] 
            i += 1