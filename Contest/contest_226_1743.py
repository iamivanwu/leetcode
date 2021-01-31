from typing import List
import collections
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        table = collections.defaultdict(list)
        counter = collections.Counter()
        for [i,j] in adjacentPairs:
            table[i].append(j)
            table[j].append(i)
            counter[i] += 1
            counter[j] += 1
        res = []
        if table:
            p = counter.most_common()[-1][0]
            last = p
            res.append(p)
            while True:
                f = False
                for point in table[p]:
                    if point != last:
                        last = p
                        p = point
                        f = True
                        break
                if not f:
                    break
                res.append(p)
        return res
adjacentPairs = [[2,1],[3,4],[3,2]]
print(Solution().restoreArray(adjacentPairs))