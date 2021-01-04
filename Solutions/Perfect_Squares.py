class Solution:
    def numSquares(self, n: int) -> int:
        arr = [n]
        level = 1
        while n > 0:
            nex =[]
            for num in arr:
                a = 1
                while a*a <= num:
                    if num - a*a == 0:
                        return level
                    nex.append(num - a*a)
                    a+= 1
            level += 1
            arr = nex
