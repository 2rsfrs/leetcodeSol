class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # make a set
        numz = set()

        # go through entire nums array and check if the char is in the set. If in the set, return True
        # if not in the set, add it to the set
        for i in nums:
            if i in numz:
                return True
            numz.add(i)

        # the entire list has been checked and no dupes have been found so return false
        return False
    
