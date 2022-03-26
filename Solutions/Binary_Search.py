from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums)-1
            mid = (l+r)//2
            while l <= r:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid
                mid = (l+r)//2
            return -1

nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2
# nums = [5]
# target = 5
print(Solution().search(nums, target))