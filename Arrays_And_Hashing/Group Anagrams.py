class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # make output list
        output = []

        # go through the list of strings
        for i in range(len(strs)):
            
            # get the sorted version of the string
            sorted_i = sorted(strs[i])

            # tracker to see if the anagram is in the output array already
            in_output = False

            # go through the output array
            for j in range(len(output)):

                # get the first string and sort it
                sorted_j = sorted(output[j][0])

                # if the current string and first string in the list are the same
                # then the current string's anagram is already in the output list
                # so add the current string to that list
                if sorted_j == sorted_i:
                    in_output = True
                    output[j].append(strs[i])

            # if the current string is not in the output list then add it to the output list
            if in_output == False:
                output.append([strs[i]])
        
        # return the output list
        return output