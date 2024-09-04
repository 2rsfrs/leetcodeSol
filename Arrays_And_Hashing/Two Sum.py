class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # sort the array
        sorted_arr = sorted(nums)

        # have a start and end ptr
        start = 0
        end = len(nums) - 1

        # for the summed numbers
        n1 = 0
        n2 = 0

        summed = 0

        # go towards the middle and check
        # if sum then set n1 and n2 to the number
        while end - start != 0 or summed != target:
            
            summed = sorted_arr[start] + sorted_arr[end]

            if summed == target:
                n1 = sorted_arr[start]
                n2 = sorted_arr[end]
                break
            
            if summed < target:
                start += 1
            
            if summed > target:
                end -= 1
        

        # find the pos of the numbers
        start = nums.index(n1)

        end = len(nums) - 1
        while nums[end] != n2:
            end -= 1

        # if the array is normal
        if start < end:
            return [start, end]
        
        # for negative numbers the array will be reversed
        return [end, start]