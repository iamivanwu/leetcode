from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        path = [[0 for i in range(0, len(obstacleGrid[0]))] for j in range(0, len(obstacleGrid))]
        for i in range(0, len(obstacleGrid)):
            for j in range(0, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    path[i][j] = 0
                    continue
                if i == 0:
                    if j > 0  and path[i][j - 1] == 0:
                        path[i][j] = 0
                    else:
                        path[i][j] = 1
                    continue
                if j == 0:
                    if i > 0 and path[i - 1][j] == 0:
                        path[i][j] = 0
                    else:
                        path[i][j] = 1
                    continue
                path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[i][j]

# a = [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
a = [[1, 0]]
sol = Solution()
print(sol.uniquePathsWithObstacles(a))