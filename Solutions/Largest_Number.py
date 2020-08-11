from typing import List
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        s = [str(x) for x in nums]
        compare = lambda a, b: 1 if a+b < b+a else -1 if a+b > b+a else 0
        return str(int(''.join(sorted(s,key=cmp_to_key(compare)))))
print(Solution().largestNumber([0,0,9,123,95]))