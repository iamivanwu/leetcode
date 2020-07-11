from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        if not nums:
            return 0
        arr = []
        for i in range(0, len(nums)):
            arr.append(nums[i])
            s = nums[i]
            for j in range(i+1,len(nums)):
                s += nums[j]
                arr.append(s)
        arr.sort()
        s = 0
        for i in range(left-1, right):
            s += arr[i]
        return  s
nums = [1,2,3,4]
n = 4
left = 3
right = 4
print(Solution().rangeSum(nums,n,left,right))
        