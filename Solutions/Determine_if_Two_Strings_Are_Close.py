from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        ct1,ct2 = Counter(word1),Counter(word2)
        v1,v2 = Counter(),Counter()
        if len(ct1) != len(ct2):
            return False
        for c in ct1:
            if c not in ct2:
                return False
            v1[ct1[c]] += 1
            v2[ct2[c]] += 1
        if len(v1) != len(v2):
            return False
        for v in v1:
            if v1[v] != v2[v]:
                return False
        return True

word1 = "aa"
word2 = "a"
# word1 = "cabbba"
# word2 = "abbccc"
print(Solution().closeStrings(word1,word2))