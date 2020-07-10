from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        maxL,maxR = height[0],height[r]
        index = 0
        area = 0
        while l < r:
            # print(index,height[index], maxL,maxR)
            if height[index] < min(maxL,maxR):
                area += min(maxL,maxR) - height[index]
            if height[l] <= height[r]:
                l += 1
                index = l
                maxL = max(maxL,height[l])
            else:
                r -= 1
                index = r
                maxR = max(maxR,height[r])
            # print(l,r,index,height[index])
        return area

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))