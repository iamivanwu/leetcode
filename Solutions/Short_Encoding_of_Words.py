from typing import List
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        s = set(words)
        for word in list(s):
            for i in range(1,len(word)):
                s.discard(word[i:])
        ans = 0
        for word in s:
            ans += len(word)+1
        return ans

words = ["time", "me", "bell"]
print(Solution().minimumLengthEncoding(words))