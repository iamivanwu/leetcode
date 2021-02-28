from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        l = len(arr)
        five =  l // 20
        return sum(arr[five:l-five])/(l-2*five)