from typing import List
class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        ans = []
        def make(now,level):
            if level == N:
                ans.append(now)
            else:
                last = int(str(now)[-1])
                if last + K < 10:
                    make(10*now+last+K,level+1)
                if last - K >= 0 and last+K != last-K:
                    make(10*now+last-K,level+1)
        for i in range(1,10):
            make(i,1)
        return ans if N > 1 else ans + [0]
print(Solution().numsSameConsecDiff(2,0))
