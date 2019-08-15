from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        limit = ((m + n) / 2)
        count = 0
        i = 0
        j = 0
        ans = 0
        end1 = False
        end2 = False
        if m == 0:
            end1 = True
        if n == 0:
            end2 = True
        flag = (m + n) % 2
        while (count < limit):
            if end1:
                ans = nums2[j]
                j += 1
            elif end2:
                ans = nums1[i]
                i += 1
            elif (not end1 and nums1[i] <= nums2[j]):
                ans = nums1[i]
                i += 1
            elif (not end2 and nums1[i] >= nums2[j]):
                ans = nums2[j]
                j += 1
            count += 1
            if i == m:
                end1 = True
                i -= 1
            if j == n:
                end2 = True
                j -= 1
        if (not flag):
            if end1:
                ans = (ans + nums2[j]) / 2
            elif end2:
                ans = (ans + nums1[i]) / 2
            elif (not end1 and nums1[i] <= nums2[j]):
                ans = (ans + nums1[i]) / 2
            elif (not end2 and nums1[i] >= nums2[j]):
                ans = (ans + nums2[j]) / 2        
        return ans


nums1 = [1, 2]
nums2 = [3, 4]
sol = Solution()
print (sol.findMedianSortedArrays(nums1, nums2))