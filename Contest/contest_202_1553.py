import collections
class Solution:
    def minDays(self, n: int) -> int:
        self.table = {}
        self.bfs([n],0)
        return self.ans
    def bfs(self,nr,level):
        if not nr:
            self.ans = level-1
            return
        nex = []
        for n in nr:
            if not n in self.table and n > 0:
                self.table[n] = 1
                nex.append(n-1) 
                if n % 2 == 0:
                    nex.append(n-n//2)
                if n % 3 == 0:
                    nex.append(n-2*(n//3))
            if n == 0:
                self.ans = level
                return
        self.bfs(nex,level+1)
print(Solution().minDays(429))        