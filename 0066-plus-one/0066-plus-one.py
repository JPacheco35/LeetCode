class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry_over = 1
        
        # traverse array from back to front        
        for num in reversed(range(len(digits))):
            
            # Case: current digit is 9 --> set digit to 0 and set 1 for carry_over
            if digits[num] == 9:
                digits[num] = (digits[num] + carry_over) % 10
                carry_over = 1
                
            # # Case: current digit is 8 and carry_over is 1 --> set digit to 0 and set 1 for carry_over
            # elif digits[num] == 8 and carry_over == 1:
            #     digits[num] = 0
            #     carry_over = 1
                
            # Otherwise: add (1+carry_over) to digit, end here because no more overflow
            else:
                digits[num] += carry_over
                return digits
        
        # if loop ends and carry_over is not 0 --> we need to add a new digit space (ie. 9 + 1 = 10)
        if carry_over == 1:
            return [1] + digits
            
        
        # we should never reach here
        return digits