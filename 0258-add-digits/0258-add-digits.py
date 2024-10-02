class Solution:
    def addDigits(self, num: int) -> int:
        
        # Case: single digit input --> return that input
        if num < 10:
            return num
        
        # get the number of digits in n
        num_digits = math.floor(math.log10(num)) + 1
        
        # loop until we only have 1 digit (n < 10)
        while num >= 10:
            
            digit_sum = 0
            
            # get each digit, add it to the sum
            for i in range(1,num_digits+1):
                digit = (num % 10**i) // 10 ** (i-1)
                digit_sum += digit
            
            
            # next loop iteration uses digit_sum's digits 
            num = digit_sum
            
            # get the number of digits in new n
            num_digits = math.floor(math.log10(num)) + 1
            
        return num