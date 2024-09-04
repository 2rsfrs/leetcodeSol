class Solution:
    def reverseBits(self, n: int) -> int:
        
        # make a returning binary string
        ret = b''

        while n != 0:
            
            # if the right most bit is 1 --> add a 1 to the binary string 
            if n & 1 == 1:
                ret += b'1'

            # if the right most bit is 0 --> add a 0 to the binary string 
            if n & 1 == 0:
                ret += b'0'
            
            # bit shift
            n = n >> 1
        
        # if the reverse string needs 0s to pad to get to 32 bits
        while len(ret) != 32:
            ret += b'0'
        
        # return the binary string as an int
        return int(ret, 2)
            
