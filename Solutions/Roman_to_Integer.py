class Solution:
    table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
    def romanToInt(self, s: str) -> int:
        ans = 0
        last = 0
        for c in reversed(s):
            num = self.table.get(c)
            if last > num:
                ans -= num
            else:
                ans += num
            last = num
        return ans


sol = Solution()
s = "MCMXCIV"
print(sol.romanToInt(s))