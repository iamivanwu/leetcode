from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.find(grid,i,j):
                    ans += 1
        return ans
    def find(self,grid,i,j):
        if i>=0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1':
            grid[i][j] = '0'
            self.find(grid,i+1,j)
            self.find(grid,i-1,j)
            self.find(grid,i,j+1)
            self.find(grid,i,j-1)
            return True
        return False