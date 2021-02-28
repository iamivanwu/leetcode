from typing import List
from collections import Counter
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        l1,l2 = len(nums1),len(nums2)
        if l1 > 6*l2 or l1*6 < l2:
            return -1
        s1,s2 = sum(nums1),sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            c1 = Counter(nums1)
            c2 = Counter(nums2)
        else:
            c1 = Counter(nums2)
            c2 = Counter(nums1)
            s1,s2 = s2,s1
        res = 0
        while s2 < s1:
            for i in range(5):
                if c1[6-i] > 0:
                    c1[6-i] -= 1
                    c1[1] += 1
                    s1 += 1 - 6 + i
                    break
                elif c2[i+1] > 0:
                    c2[i+1] -= 1
                    c2[6] += 1
                    s2 += 6 - i - 1
                    break
            res += 1
        return res
nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]
nums1 = [3,3,2,4,2,6,2]
nums2 = [6,2,6,6,1,1,4,6,4,6,2,5,4,2,1]
print(Solution().minOperations(nums1,nums2))