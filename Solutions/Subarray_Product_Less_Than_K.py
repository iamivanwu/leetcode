from typing import List
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        m = 1
        c = 0
        # if k < 1 :
        #     return 0
        for i in range(len(nums)):
            m *= nums[i]
            while m >= k and l <= i:
                m //= nums[l]
                l += 1
            c += i - l + 1
        return c

nums = [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
# nums = [1,2,3]
k = 19
sol = Solution()
print(sol.numSubarrayProductLessThanK(nums,k))