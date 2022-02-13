from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(perm, arr):
            if not arr:
                ans.append(perm)
            for i in range(0, len(arr)):                    
                dfs(perm+[arr[i]], arr[0:i]+arr[i+1:])
        dfs([], nums)
        return ans       
num = [1,2,3]
print(Solution().permute(num))