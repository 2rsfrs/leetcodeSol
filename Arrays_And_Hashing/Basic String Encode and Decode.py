class Solution:

    # encode by adding #n where n is the len of the string before each word
    def encode(self, strs: List[str]) -> str:

        ret = ""

        for i in strs:
            size = len(i)
            ret += str(size) + "#" + i
        
        return ret

    # decode by searching for the # and checking the indices before for the len
    # of the original string
    def decode(self, s: str) -> List[str]:

        ret = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1
            
            # size could be more than 1 digit so we cannot just check the previous
            # index
            size = int(s[i:j])
            string = s[j + 1: j+size+1]

            ret.append(string)

            i = j + size + 1
        
        return ret

