class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0 for i in range(0, m)] for j in range(0, n)]
        for i in range(0, n):
            for j in range(0, m):
                if i == 0:
                    path[i][j] = 1
                    continue
                if j == 0:
                    path[i][j] = 1
                    continue
                path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[i][j]
# 1 1 1  1  1  1  1
# 1 2 3  4  5  6  7
# 1 3 6 10 15 21 28

m = 7
n = 3
sol = Solution()
print(sol.uniquePaths(m, n))