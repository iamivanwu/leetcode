from typing import List
class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        cstack = []
        if len(s) > 0:
            cstack.append(cost[0])
        for i in range(1,len(s)):
            cstack.append(cost[i])
            if s[i] == s[i-1]:
                ans += min(cstack[-1],cstack[-2])
                if cstack[-1] > cstack[-2]:
                    cstack.pop(-2)
                else:
                    cstack.pop(-1)
        return ans
s = "aaabbbabbbb"
cost = [3,5,10,7,5,3,5,5,4,8,1]
print(Solution().minCost(s,cost))