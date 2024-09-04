class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # if nums does not have any elements return 0
        if not nums:
            return 0

        # make the list a set then make the set into a sorted list
        sorted_list = sorted(list(set(nums)))
        
        # set the current max to 1 by default
        curr_max = 1

        # go through the sorted list
        # curr is the current consecutive sequence count
        # if the next number is in the consecutive sequence, add 1 to curr
        # if the next number is not in the consecutive sequence, set the max equal to
        # the max of the current max or the current count
        i = 0
        curr = 1
        while i < len(sorted_list)-1:

            if sorted_list[i] + 1 == sorted_list[i+1]:
                curr += 1
            
            else:
                curr_max = max(curr_max, curr)
                curr = 1

            i += 1
        
        # final check and return the max
        curr_max = max(curr_max, curr)
        return curr_max