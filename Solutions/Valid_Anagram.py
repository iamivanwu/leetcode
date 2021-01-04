import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = collections.Counter(s)
        b = collections.Counter(t)
        if len(a) == len(b):
            for letter in a:
                if a[letter] != b[letter]:
                    return False
            return True
        return False 
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s,t))