class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # begin with carry_over at 1 because we are adding 1 to the original number
        carry_over = 1
        
        # traverse array from back to front        
        for num in reversed(range(len(digits))):
            
            # Case: current digit is 9 --> set digit to 0, carry_over remains 1
            if digits[num] == 9:
                digits[num] = 0
                
            # Otherwise: just add carry_over to digit, end here because there is no more overflow
            else:
                digits[num] += carry_over
                return digits
        
        # if loop ends and carry_over is not 0 --> we need to add a new digit space (ie. 9 + 1 = 10)
        if carry_over == 1:
            return [1] + digits
            
        
        # we should never reach here
        return digits