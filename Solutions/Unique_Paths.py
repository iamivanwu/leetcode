class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1
        b = n - 1
        if a < b:
            temp = a
            a = b
            b = temp
        c = m + n - 2
        s = 1
        j = 1
        for i in range(a + b, a, -1):
            s = (s * i) / j
            j += 1
        return int(s)

m = 3
n = 2
sol = Solution()
print(sol.uniquePaths(m, n))