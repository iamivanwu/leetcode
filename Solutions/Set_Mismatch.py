from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = {}
        dup,total = 0,0
        for n in nums:
            if n in dic:
                dup = n
            else:
                dic[n] = 1 
                total += n
        return [dup, len(nums)*(len(nums)+1)//2 - total]