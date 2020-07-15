from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return []
        row = []
        column = []
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)
        for i in row:
            matrix[i] = [0 for _ in range(0,len(matrix[0]))]
        for j in column:
            for i in range(0,len(matrix)):
                matrix[i][j] = 0
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Solution().setZeroes(matrix)
print(matrix)
