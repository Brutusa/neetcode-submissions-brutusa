class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if different lengths
        # return false
        if len(s) != len(t):
            return False

        # sort strings
        # compare strings
        s_sorted = sorted(s)
        t_sorted = sorted(t)

        if s_sorted == t_sorted:
            return True
        return False
