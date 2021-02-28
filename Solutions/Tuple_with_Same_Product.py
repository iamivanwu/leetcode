from typing import List
from collections import Counter
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = Counter()
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                counter[nums[i]*nums[j]] += 1
        res = 0
        for c in counter:
            if counter[c] > 1:
                res += counter[c]*(counter[c]-1)//2
        return res*8
nums = [2,3,4,6,8,12]
print(Solution().tupleSameProduct(nums))