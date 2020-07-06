from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        # for i in range (0, len(height)-1):
        #     for j in range(1,len(height)):
        #         if (j-i)*min(height[i],height[j]) > m:
        #             m = (j-i)*min(height[i],height[j])
        # return m
        left = 0
        right = len(height)-1
        for _ in range(0, len(height)-1):
            if (right-left)*min(height[left],height[right]) > m:
                m = (right-left)*min(height[left],height[right])
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            if left == right:
                break
        return m

sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [1,1]
print(sol.maxArea(height))