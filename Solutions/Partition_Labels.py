from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        t = {}
        for i in range(len(s)):
            if s[i] in t:
                t[s[i]][1] = i
            else:
                t[s[i]] = [i, i]
        start, end = 0, 0
        for i in range(len(s)):
            end = max(t[s[i]][1], end)
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res
