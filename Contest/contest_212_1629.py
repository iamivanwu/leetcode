from typing import List
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        if not keysPressed:
            return ''
        temp = 0
        m,mt = 0,'a'
        for i in range(len(releaseTimes)):
            dist = releaseTimes[i] - temp
            if dist > m:
                mt = keysPressed[i]
                m = dist
            elif dist == m:
                mt = max(mt,keysPressed[i])
            temp = releaseTimes[i]
        return mt