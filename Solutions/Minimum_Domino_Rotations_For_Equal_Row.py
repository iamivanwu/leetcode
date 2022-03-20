from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        same = [tops[0], bottoms[0]]
        count = [0, 0]
        c = 0
        for i in range(1, len(tops)):
            if tops[i] != same[0] and bottoms[i] != same[0]:
                same[0] = -1
            if tops[i] != same[1] and bottoms[i] != same[1]:
                same[1] = -1
            if tops[i] != bottoms[i]:
                if tops[i] != same[0] and bottoms[i] == same[0]:
                    count[0] += 1
                if tops[i] == same[1] and bottoms[i] != same[1]:
                    count[1] += 1
            else:
                c += 1

            if same[0] == -1 and same[1] == -1:
                return -1
        ans = len(tops) + 1
        if same[0] != -1:
            ans = min(ans, count[0], len(tops) - c - count[0])
        if same[1] != -1:
            ans = min(ans, count[1], len(tops) - c - count[1])
        return ans if ans > 0 else 0


tops = [2, 2, 2, 2, 3]
bottoms = [3, 3, 3, 3, 3]
tops = [1, 1, 2]
bottoms = [1, 2, 1]
print(Solution().minDominoRotations(tops, bottoms))
