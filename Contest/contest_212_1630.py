from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(arr):
            if len(arr) < 3:
                return True
            d = arr[1] - arr[0]
            for i in range(2,len(arr)):
                if arr[i] - arr[i-1] != d:
                    return False
            return True
        res = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            arr.sort()
            if not check(arr):
                res.append('false')
            else:
                res.append('true') 
        return res