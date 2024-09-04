class Solution:
    def countBits(self, n: int) -> List[int]:
        
        # helper to count the number of 1 bits for a number n
        def helper(n: int) -> int:
            
            counter = 0
            while n != 0:
                if n & 1 == 1:
                    counter += 1
                
                n = n >> 1
            
            return counter
        
        ret = []

        # go from [0-n] and count the number of 1s for each number and add to 
        # return list
        for i in range(n+1):
            num = helper(i)
            ret.append(num)
        
        return ret
