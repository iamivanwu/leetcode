from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        non = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
            else:
                if non != i:
                    nums[non],nums[i] = nums[i],nums[non]
                non += 1
        for i in range(len(nums)-zero,len(nums)):
            nums[i] = 0
nums = [0,1,0,3,12]