from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist = {}
        for i in range(len(nums)):
            if target-nums[i] in dist:
                return [dist[target-nums[i]],i]
            else:
                dist[nums[i]] = i
nums = [3,2,4]
target = 6
nums = [2,7,11,15]
target = 9
print (Solution().twoSum(nums,target))