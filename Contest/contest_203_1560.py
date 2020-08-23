from typing import List
import collections
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        last = rounds[0]
        table = collections.Counter()
        table[rounds[0]] += 1
        for i in range(1,len(rounds)):
            if last < rounds[i]:
                for j in range(last+1,rounds[i]+1):
                    table[j] += 1
            else:
                for j in range(last+1,n+1):
                    table[j] += 1
                for j in range(1,rounds[i]+1):
                    table[j] += 1
            last = rounds[i]
        m = max(table.values())
        ans = []
        for key in table:
            if table[key] == m:
                ans.append(key)
        return sorted(ans)
n = 2
rounds = [2,1,2,1,2,1,2,1,2]
n = 4
rounds = [1,3,1,2]
print(Solution().mostVisited(n,rounds))