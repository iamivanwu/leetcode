from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squ = {}
        col = {}
        for j in range(0,9):
            row = {}
            for i in range(0,9):
                if row.get(board[j][i]):
                    return False
                if j == 0:
                    col[i] = {}
                if col[i].get(board[j][i]):
                    return False
                if not squ.get(3*(j//3)+i//3):
                    squ[3*(j//3)+i//3] = {}
                if squ[3*(j//3)+i//3].get(board[j][i]):
                    return False
                if board[j][i] != '.':
                    row[board[j][i]] = 1
                    col[i][board[j][i]] = 1
                    squ[3*(j//3)+i//3][board[j][i]] = 1            
        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(board))