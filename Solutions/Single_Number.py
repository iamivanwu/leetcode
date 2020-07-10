from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if not dic.get(i):
                dic[i] = 1
            else:
                dic.pop(i)
        for i in dic:
            return i

nums = [2,2,3]
print(Solution().singleNumber(nums))