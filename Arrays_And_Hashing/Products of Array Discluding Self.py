class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        zero_count = 0
        
        # go through and get the product of all numbers
        for i in nums:
            if i != 0:
                product *= i
            
            # if there is a 0 do not multiply it and add a count
            if i == 0:
                zero_count += 1

        # if the whole list is full of 0s, return the list
        if zero_count == len(nums):
            return nums

        ret = []

        # go through the list of nums
        for i in range(len(nums)):

            # if there is exactly 1 0, make every entry 0 except for the index 
            # that originally has the 0
            if zero_count == 1:

                if nums[i] != 0:
                    ret.append(0)
                else:
                    ret.append(product)
            
            # if there is more than 1 0, return an array with the same len as nums
            # but full of 0s
            elif zero_count > 1:
                return [0 for _ in range(len(nums))]
            
            # any other situation, divide the product by the number at index i
            else:
                ret.append(product // nums[i])
        
        return ret