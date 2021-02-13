from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] or grid[l-1][l-1]:
            return -1
        bfs = [(0,0,1)]
        grid[0][0] = 1
        for i,j,d in bfs:
            if i == l-1 and j == l-1:
                return d
            for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < l and 0 <= y < l and grid[x][y] == 0:
                    grid[x][y] = 1
                    bfs.append((x,y,d+1))
        return -1