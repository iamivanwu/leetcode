from typing import List
import math
class Solution:
    table = {
        '2' : ['a','b','c'],
        '3' : ['d','e','f'],
        '4' : ['g','h','i'],
        '5' : ['j','k','l'],
        '6' : ['m','n','o'],
        '7' : ['p','q','r','s'],
        '8' : ['t','u','v'],
        '9' : ['w','x','y','z'],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        self.out = []
        self.length = len(digits)
        self.dig = digits
        try:
            for i in self.table.get(digits[0]):
                self.getStr(i,1)
            return self.out
        except:
            return self.out
    def getStr(self, s, index):
        if index == self.length:
            return self.out.append(s)
        for letter in self.table.get(self.dig[index]):
            self.getStr(s+letter,index+1)

digits = "23"
print(Solution().letterCombinations(digits))