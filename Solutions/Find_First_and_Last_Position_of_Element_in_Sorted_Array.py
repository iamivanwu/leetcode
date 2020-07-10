from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:            
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums)-1    
        left = -1
        right = -1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target and (nums[mid-1] != target or mid == 0) :
                left = mid
                break
            elif nums[mid] > target or nums[mid] == target:
                r = mid - 1
            else:
                l = mid + 1
        l,r = 0,len(nums)-1
        while l <= r:
            mid = (r+l)//2
            if nums[mid] == target and (mid+1==len(nums) or nums[mid+1] != target):
                right = mid
                break
            elif nums[mid] < target or nums[mid] == target:
                l = mid + 1
            else:
                r = mid - 1
        return [left,right]


nums = [5,7,7,8,8,10]
target = 8
print(Solution().searchRange(nums,target))