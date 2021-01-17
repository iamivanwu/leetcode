from typing import List
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        arr = []
        m = 0
        for rect in rectangles:
            m = max(m,min(rect))
            arr.append(min(rect))
        count = 0
        for a in arr:
            if m == a:
                count += 1
        return count