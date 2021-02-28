from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        out = ['']*len(s)
        for i in range(len(s)):
            out[indices[i]] = s[i]
        return "".join(out)
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(Solution().restoreString(s,indices))