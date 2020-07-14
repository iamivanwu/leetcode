from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        a = []
        start,last = -1,-1
        intervals.sort()
        for i in range(0,len(intervals)):
            if start == -1:
                a.append(intervals[i])
                start,last = intervals[i][0],intervals[i][1]
            elif intervals[i][0] <= last:
                last = max(intervals[i][1],last)
                a[-1] = [start,last]
            else:
                start = intervals[i][0]
                last = intervals[i][1]
                a.append([start,last])
        return a
intervals = [[1,4],[0,4]]
print(Solution().merge(intervals))
