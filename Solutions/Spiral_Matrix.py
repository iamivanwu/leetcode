from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        if not matrix:
            return out
        x,y = 0,-1
        direction = 1
        while len(out) < len(matrix)*len(matrix[0]):
            if direction == 1:
                if y+1 < len(matrix[0]) and matrix[x][y+1] != '':
                    y += 1
                    out.append(matrix[x][y])
                    matrix[x][y] = ''
                else:
                    direction = 2
            if direction == 2:
                if x+1 < len(matrix) and matrix[x+1][y] != '':
                    x += 1
                    out.append(matrix[x][y])
                    matrix[x][y] = ''
                else:
                    direction = 3
            if direction == 3:
                if y-1 > -1 and matrix[x][y-1] != '':
                    y -= 1
                    out.append(matrix[x][y])
                    matrix[x][y] = ''
                else:
                    direction = 4
            if direction == 4:
                if x-1 > -1 and matrix[x-1][y] != '':
                    x -= 1
                    out.append(matrix[x][y])
                    matrix[x][y] = ''
                else:
                    direction = 1
        return out
# better:
# append four direction in one loop
# top -- left ++ right -- botton ++
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
print(Solution().spiralOrder(matrix))
        