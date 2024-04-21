class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_chars = list()
        t_chars = list()

        for c in s:
            s_chars.append(c)

        for c in t:
            t_chars.append(c)
        
        s_chars.sort()
        t_chars.sort()

        # just return s_chars == t_chars silly!
        return s_chars == t_chars
        # if s_chars == t_chars:
        #     return True
        # return False