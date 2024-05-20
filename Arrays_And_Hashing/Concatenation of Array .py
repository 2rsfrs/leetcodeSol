class Solution:
    def getConcatenation(self, nums):
        
        # make answer list
        ans = []
        # loop through twice and add to ans
        for i in range(2):
            for num in nums:
                ans.append(num)
        # return ans
        return ans
    
    def better(self, nums):
        return nums*2