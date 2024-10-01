class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # traverse array from back to front        
        for num in reversed(range(len(digits))):
            
            # Case: current digit is 9 --> set digit to 0, carry over 1 to next position
            if digits[num] == 9:
                digits[num] = 0
                
            # Otherwise: just add 1 to digit, end here because there is no more overflow
            else:
                digits[num] += 1
                return digits
        
        # if we reach here, need to add a new digit space (ie. 9 + 1 = 10)
        return [1] + digits