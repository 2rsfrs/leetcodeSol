class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # sort nums
        nums = sorted(nums)

        # go through the array and if the number is not the same as the index
        # that is the missing number
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        # if all numbers are there, n is missing
        return len(nums)
