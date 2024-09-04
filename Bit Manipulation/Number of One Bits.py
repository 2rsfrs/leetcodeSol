class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
        # go through the number
        while n != 0:

            # if the rightmost bit is a 1 add 1 to the counter
            if n & 1 == 1:
                counter += 1
            
            # bit shift
            n = n >> 1
        
        # return the number of 1s
        return counter