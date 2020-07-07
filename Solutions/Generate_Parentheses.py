from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.num = n
        self.generate('',0,0)
        return self.ans
    def generate(self, s, left, right):
        print(left,right)
        if left == self.num and right == self.num:
            self.ans.append(s)
        if left >= right:
            if left < self.num:
                self.generate(s+'(',left+1,right)
            self.generate(s+')',left,right+1)
        
print(Solution().generateParenthesis(3))