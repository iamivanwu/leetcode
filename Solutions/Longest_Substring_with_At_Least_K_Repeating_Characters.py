class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in s:
            if s.count(c) < k:
                return max(self.longestSubstring(sub,k) for sub in s.split(c))
        return len(s)
s = "aaabbcde"
k = 3
print(Solution().longestSubstring(s,k))