from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        a = []
        def go(index,path):
            a.append(path)
            for i in range(index, len(nums)):
                print(i)
                go(i+1,path+[nums[i]])
        go(0,[])
        return a
nums = [1,2,3,4,5,6,7,8,10,0]
print(Solution().subsets(nums))
