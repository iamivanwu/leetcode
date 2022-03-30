from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # need rewrite


        for i in range(len(nums)):
            if nums[i] == target:
                return True
        return False


nums = [1, 0, 1, 1, 1]
target = 0
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
target = 2
nums = [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
target = 13
print(Solution().search(nums, target))
