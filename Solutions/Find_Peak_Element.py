from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l,r = 0,len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
nums = [3,2,1]
print(Solution().findPeakElement(nums))