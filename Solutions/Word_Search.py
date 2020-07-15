from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if self.go(board,i,j,word):
                    return True
        return False
    def go(self,board,x,y,w):
        if len(w) == 0 or (board[x][y] == w[0] and len(w) == 1):
            return True
        if board[x][y] != w[0]:
            return False
        res = False
        c = board[x][y]
        board[x][y] = ''
        if x+1 < len(board):
            res = self.go(board,x+1,y,w[1:])
        if not res and x-1 > -1:
            res = self.go(board,x-1,y,w[1:])
        if not res and y+1 < len(board[0]):
            res = self.go(board,x,y+1,w[1:]) 
        if not res and y-1 > -1:
            res = self.go(board,x,y-1,w[1:])
        board[x][y] = c
        return res 
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board = [["a"]]
word = "a"
print(Solution().exist(board,word))