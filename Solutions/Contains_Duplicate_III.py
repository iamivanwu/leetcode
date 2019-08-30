from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,i+k+1):
                if j < len(nums):
                    if abs(nums[i] - nums[j]) <= t:
                        return True
        return False


nums, k, t = [1,2,3,1], 3, 0
nums, k, t = [1,0,1,1], 1, 2
nums, k, t = [1,5,9,1,5,9], 2, 3
# nums, k, t = [0], 0, 0
# nums, k, t = [2,4], 1, 1
# nums, k, t = [-1,-1], 1, -1
nums, k, t = [3,6,0,4], 2, 2
sol = Solution()
print(sol.containsNearbyAlmostDuplicate(nums, k, t))