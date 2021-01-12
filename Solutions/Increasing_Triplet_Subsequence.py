from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        smaller = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= smaller:
                smaller = num
            else:
                return True
        return False
nums = [1,1,1,1,1]
print(Solution().increasingTriplet(nums))