from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        length = len(grid)
        maxXList = []
        maxYList = []
        for i in range(0, length):
            maxXList.append(max(grid[i]))
            maxY = 0
            for j in range(0, length):
                if grid[j][i] > maxY:
                    maxY = grid[j][i]
            maxYList.append(maxY)
        print(maxXList, maxYList)
        sum = 0
        for i in range(0, length):
            for j in range(0, length):
                sum = sum + min(maxYList[i],maxXList[j]) - grid[i][j]
        return sum

a = [ [3, 0, 8, 4], 
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]
sol = Solution()
print(sol.maxIncreaseKeepingSkyline(a))