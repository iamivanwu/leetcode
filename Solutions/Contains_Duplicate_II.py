from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        if len(nums) == 0:
            return False
        for i in range(0, len(nums)):
            if record.get(nums[i]) != None and  i - record.get(nums[i]) <= k:
                return True
            record.update({nums[i]: i})
        return False


nums, k = [1,2,3,1], 3
nums, k = [1,0,1,1], 1
nums, k = [99,99], 2
nums, k = [1,2,3,1,2,3], 2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))