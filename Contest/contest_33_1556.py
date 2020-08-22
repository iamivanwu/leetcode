class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        index = 0
        ans = ''
        for c in s[::-1]:
            if index > 0 and index % 3 == 0:
                ans = '.' + ans
            ans = c + ans
            index += 1
        return ans
print(Solution().thousandSeparator(51040))