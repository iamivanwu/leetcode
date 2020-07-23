from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        f = [False]*len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (f[i-len(w)] or i-len(w) == -1):
                    f[i] = True
        return f[-1]

s = "leetcode"  
wordDict = ["leet", "code"]
print(Solution().wordBreak(s,wordDict))