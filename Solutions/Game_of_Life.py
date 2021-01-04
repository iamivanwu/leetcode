from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(i,j):
            count = 0
            for m in range(max(0,i-1),min(len(board),i+2)):
                for n in range(max(0,j-1),min(len(board[0]),j+2)):
                    if not (m == i and n == j):
                        count += board[m][n] & 1
            if board[i][j]:
                if count == 2 or count == 3:
                    board[i][j] += 2
            else:
                if count == 3:
                    board[i][j] += 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                check(i,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
print(Solution().gameOfLife(board))