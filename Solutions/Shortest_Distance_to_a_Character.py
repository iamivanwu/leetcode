from typing import List
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        count = 0
        for i in range(len(s)):
            if s[i] == c:
                if not res:
                    for _ in range(count):
                        res.append(count)
                        count -= 1
                else:
                    dist = [0]*count
                    d = 1
                    for half in range((count+1)//2):
                        dist[half] = dist[count-1-half] = d
                        d += 1
                    res = res + dist
                res.append(0)
                count = 0
            else:
                count += 1
        if count:
            for j in range(count):
                res.append(j+1)
        return res
s = "loveleetcode"
c = "e"
print(Solution().shortestToChar(s,c))