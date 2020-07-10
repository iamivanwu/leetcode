from typing import List
class Solution:
    ans = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        self.ans = []
        for i in range(0, len(nums)):
            self.recur([],i,nums)
        return self.ans
    def recur(self,now,index,nums:List[int]):
        now.append(nums[index])
        a = nums.copy()
        a.pop(index)
        if not a:
            self.ans.append(now)
            return
        for i in range(0,len(a)):
            self.recur(now.copy(),i,a)

num = [1,2,3]
print(Solution().permute(num))