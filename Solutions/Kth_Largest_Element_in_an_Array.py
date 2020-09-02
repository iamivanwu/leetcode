from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:   
        def quickSelect(arr: List[int], start, end, k):
            if start < end:
                fix = arr[start]
                l = start
                for i in range(start+1,end):
                    if arr[i] < fix:
                        l += 1
                        arr[i],arr[l] = arr[l],arr[i]
                arr[start],arr[l] = arr[l],arr[start]
                # print(arr,fix,l,start,end)
                print(end-l,k)
                if end-l < k:
                    return quickSelect(arr,start,l,k-end+l)
                elif end - l == k:
                    return arr[l]
                else:
                    return quickSelect(arr,l+1,end,k)
        quickSelect(nums,0,len(nums),k)
        return nums[-k]
num = [3,2,3,1,2,4,5,5,6]
# num = [3,2,1,5,6,4]
# num = [5,6,4]
# num = [5,3,12,1,23,43,2,6]
k = 2
print(Solution().findKthLargest(num,k))