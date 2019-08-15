from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        count = 0
        for i in range (0 , len(nums) - 2):
            if (nums[i] > 0):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            l,r = i + 1,len(nums) -1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if (s < 0):
                    l += 1
                elif (s > 0):
                    r -= 1
                else:
                    ans.append((nums[i],nums[l],nums[r]))
                    while l < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r and nums[r - 1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans

# sol = Solution()
# test = [1,-2,-5,-13,-10,-11,0,-12,-11,13,-4,9,8,10,-7,3,-9,-12,-7,8,-2,-12,1,-10,-15,-8,5,14,-7,-8,-8,9,-3,-6,3,-5,-1,-11,-10,3,-13,1,-10,3,-12,-10,-9,-13,-7,-1,10,6,-6,-12,12,-13,-13,-6,-14,-13,-7,-7,4,6,-6,-8,8,8,-4,13,-11,-1,-8,-14,9,-5,-9,7,-3,-1,14,14,13,-7,9,2,-5,12,11,-12,14,-11,-12,3,2,-2,3,-5,-9,14,-14,-13,-10,-7,-12,14,3,-6,-1,8,1,-2,-1,-1,6,-6]
# print (sol.threeSum([-1,0,1,2,-1,-4]))
# print (sol.threeSum([1,-1,-1,0]))
# print (sol.threeSum(test))