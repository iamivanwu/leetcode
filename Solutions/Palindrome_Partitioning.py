from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all = []
        self.find(s,[],all)
        return all
    def find(self,s,part,all: list):
        if not s:
            all.append(part)
        else:
            for i in range(1,len(s)+1):
                if self.isPal(s[:i]):
                    self.find(s[i:],part+[s[:i]],all)
    def isPal(self,s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
s = "aabcc"
print(Solution().partition(s))