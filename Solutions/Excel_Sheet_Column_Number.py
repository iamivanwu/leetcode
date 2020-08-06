class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 1
        for c in s:
            ans += (ord(c)-ord('A')+1)*n
            n *= 26
        return ans