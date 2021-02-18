from typing import List
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        def cal(n):
            return (1+n-2)*(n-2)//2
        res,d,count = 0,-1,0
        for i in range(1,len(A)):
            if A[i] - A[i-1] == d:
                count += 1
            else:
                if count >= 2:
                    res += cal(count+1)
                d = A[i] - A[i-1]
                count = 1
        if count >= 2:
            res += cal(count+1)
        return res