from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) == 0 or k == 0:
            return False
        if len(nums) <= k :
            nums.sort()
            temp = nums[0]
            for i in range(1 ,len(nums)):
                if (abs(temp - nums[i]) <= t):
                    print(abs(temp - nums[i]))
                    return True
                temp = nums[i]
        else :
            tempList = []
            temp = nums[k - 1]
            for i in range(k):
                tempList.append(nums[i])
                if (abs(temp - nums[i]) <= t and k > 1):
                    return True
                temp = nums[i]
            print(tempList)
            for i in range(k, len(nums)):
                for j in range(len(tempList)):
                    if(abs(nums[i] - tempList[j]) <= t):
                        return True
                tempList.pop(0)
                tempList.append(nums[i])
        return False

nums, k, t = [1,2,3,1], 3, 0
nums, k, t = [1,0,1,1], 1, 2
# nums, k, t = [1,5,9,1,5,9], 2, 3
nums, k, t = [0], 0, 0
nums, k, t = [2,4], 1, 1
sol = Solution()
print(sol.containsNearbyAlmostDuplicate(nums, k, t))