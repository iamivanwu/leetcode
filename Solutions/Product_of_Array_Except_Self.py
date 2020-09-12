from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r,ans = [0]*len(nums),[0]*len(nums),[0]*len(nums)
        l[0] = 1
        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]
        r[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1):
            r[i] = r[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i] = l[i]*r[i]
        return ans