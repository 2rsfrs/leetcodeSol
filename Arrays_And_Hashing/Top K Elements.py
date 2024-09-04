class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # helper function to get the biggest value in the dictionary
        # returns the biggest key
        def getBiggest(d: dict):

            big_key = 0
            big_value = 0
            for i in d.keys():
                if d[i] > big_value:
                    big_key = i
                    big_value = d[i]
            
            return big_key

        numbs = dict()

        # go through list of numbers and get a count for each number
        for i in nums:
            
            if i not in numbs:
                numbs[i] = 1
            
            else:
                numbs[i] += 1
        
        # get the k biggest keys from the dictionary
        # add the biggest key to the return list then remove it so the next
        # iteration can find the next biggest key
        ret = []
        while k != 0:
            big_key = getBiggest(numbs)
            ret.append(big_key)
            del numbs[big_key]
            k -= 1

        return ret