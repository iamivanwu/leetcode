from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        unit = 0
        rev = []
        for n,u in boxTypes:
            rev.append([u,n])
        rev.sort(reverse=True)
        while truckSize > 0:
            if rev:
                if rev[0][1] < truckSize:
                    unit += rev[0][0]*rev[0][1]
                    truckSize -= rev[0][1]
                    rev.pop(0)
                else:
                    unit += rev[0][0]*truckSize
                    truckSize = 0
            else:
                break
        return unit
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
print(Solution().maximumUnits(boxTypes,truckSize))