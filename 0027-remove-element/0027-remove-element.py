class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # loop through each numebr
        for num in reversed(nums):
            
            # remove val if detected, add 1 to removed counter
            if num == val:
                nums.remove(num)
                
        # return number of items remaining
        return len(nums)