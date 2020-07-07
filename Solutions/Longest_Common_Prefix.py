from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        try:
            for i in range(0, len(strs[0])):
                for j in range(1,len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return ans
                ans += strs[0][i]
            return ans
        except:
            return ans



strs = ["flower","flow","flight"]
strs = []
sol = Solution()
print(sol.longestCommonPrefix(strs))