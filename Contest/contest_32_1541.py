class Solution:
    def minInsertions(self, s: str) -> int:
        n = 0
        ans = 0
        for c in s:
            if c == '(':
                if n % 2 == 1:
                    ans += 1
                    n -= 1
                n += 2
            else:
                n -= 1
            if n < 0:
                ans += 1
                n += 2
        return ans + n
s = "(()))(()))()())))"