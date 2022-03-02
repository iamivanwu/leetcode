class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        if len(s) == 0:
            return True
        for c in t:
            if c == s[index]:
                index += 1
            if index == len(s):
                return True
        return False