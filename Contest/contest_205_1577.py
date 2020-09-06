from typing import List
import collections
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        table_1 = collections.Counter()
        table_2 = collections.Counter()
        for i in range(len(nums1)-1):
            for j in range(i+1,len(nums1)):
                table_1[nums1[i]*nums1[j]] += 1
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                table_2[nums2[i]*nums2[j]] += 1
        ans = 0
        for n in nums1:
            ans += table_2[n*n]
        for n in nums2:
            ans += table_1[n*n]
        return ans
nums1 = [7,4]
nums2 = [5,2,8,9]
print(Solution().numTriplets(nums1,nums2))