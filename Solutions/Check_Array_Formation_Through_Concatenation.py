from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        i = 0
        while i < len(arr):
            flag = False
            add = False
            for piece in pieces:
                if piece[0] == arr[i]:
                    flag = True
                    for p in piece:
                        if i<len(arr) and p == arr[i]:
                            if i+1 <= len(arr):
                                add = True
                                i += 1
                        else:
                            return False
                    break
            if not add:
                i += 1
            if not flag:
                return False
        return True
arr = [91,4,64,78]
pieces = [[78],[4,64],[91]]
arr = [37,69,3,74,46]
pieces = [[37,69,3,74,46]]
print(Solution().canFormArray(arr,pieces))