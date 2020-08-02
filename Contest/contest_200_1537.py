from typing import List
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        f,s = 0,0
        p1,p2 = 0,0
        while f < len(nums1) or s < len(nums2):
            if f >= len(nums1):
                p2 += nums2[s]
                s += 1
                continue
            elif s >= len(nums2):
                p1 += nums1[f]
                f += 1
                continue           
            if nums1[f] < nums2[s]:
                p1 += nums1[f]
                f += 1
            elif f > len(nums1) or nums1[f] > nums2[s]:
                p2 += nums2[s]
                s += 1
            else:
                m = max(p1+nums1[f],p2 + nums2[s])
                p1 = m
                p2 = m
                f += 1
                s += 1
        return max(p1,p2) % 1000000007
nums1 = [2,4,5,8,10]
nums2 = [4,6,8,9]

print(Solution().maxSum(nums1,nums2))