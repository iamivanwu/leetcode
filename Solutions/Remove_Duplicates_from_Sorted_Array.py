from typing import List
# Definition for singly-linked list.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[index]:
                index += 1
                nums[index] = nums[i]
        return index+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums))
print(nums)