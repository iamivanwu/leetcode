from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Flip upside down, than symmetry
        for i in range(0,len(matrix)//2):
            for j in range(0,len(matrix[i])):
                matrix[i][j],matrix[len(matrix)-1-i][j] = matrix[len(matrix)-1-i][j],matrix[i][j]
        print(matrix)
        for i in range(0,len(matrix)):
            for j in range(0,i):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
# matrix = [
#   [ 5, 1, 9,11,7],
#   [ 2, 4, 8,10,7],
#   [13, 3, 6, 7,7],
#   [15,14,12,16,7],
#   [0,0,0,0,0]
# ]
Solution().rotate(matrix)
print(matrix)