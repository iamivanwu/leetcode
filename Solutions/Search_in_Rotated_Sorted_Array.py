from typing import List
import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # -->
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1



nums = [4,5,6,7,0,1,2]
target = 4
# nums = [8,1,2,3,4,5,6,7]
# target = 6
# nums = [1,2,3,4]
# target = 3
# nums = [1,3,5]
# target = 5
# nums = []
# target = 5
# nums = [1]
# target = 0
print(Solution().search(nums,target))