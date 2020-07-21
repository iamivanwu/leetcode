from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        outer = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1:
                    if board[i][j] == 'O':
                        outer.append((i,j))
        while outer:
            (x,y) = outer.pop(0)
            if -1 < x < len(board) and -1 < y < len(board[0]) and board[x][y] == 'O':
                board[x][y] = '*'
                outer.append((x,y+1))
                outer.append((x,y-1))
                outer.append((x+1,y))
                outer.append((x-1,y))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(board)
print(board)