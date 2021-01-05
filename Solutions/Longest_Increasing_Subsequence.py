from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            if not dp:
                dp.append([n,1])
            else:
                count = 1
                for d in dp:
                    if n > d[0]:
                        count = max(count,d[1]+1)
                dp.append([n,count])
        return max(dp,key=lambda x:x[1])[1]
nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))