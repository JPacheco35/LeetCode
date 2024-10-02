class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        # get the number of digits in n
        num_digits = math.floor(math.log10(n)) + 1
        
        # loop until we reach either 1 (HN) or 4 (NOT HN)
        while True:
            
            square_sum = 0
            
            # get each digit, add its sqaure to the sum
            for i in range(1,num_digits+1):
                digit = (n % 10**i) // 10 ** (i-1)
                square_sum += digit ** 2
            
            # Case: NOT Happy Number --> False
            if square_sum == 4:
                return False
            
            # Case: Happy Number --> True
            if square_sum == 1:
                return True
            
            # next loop iteration uses square_sum's digits 
            n = square_sum
            
            # get the number of digits in new n
            num_digits = math.floor(math.log10(n)) + 1
            
            
        
        
        # we should never reach here
        return True