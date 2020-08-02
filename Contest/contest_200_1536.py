from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for i in range(0,n):
            count = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
        step = 0
        check = 0
        print(zeros)
        while check <= n-1:
            flag = False
            for i in range(check,n):
                if zeros[i] >= n-check-1:
                    num = zeros.pop(i)
                    zeros.insert(check,num)
                    step += i - check
                    check += 1
                    flag = True
                    break
            if not flag:
                return -1

            # if max(zeros[check:]) >= n - check - 1:
            #     index = zeros[check:].index(max(zeros[check:])) + check
            #     num = zeros[index]
            #     zeros.pop(index)
            #     zeros.insert(check,num)
            #     print(check,index)
            #     step += index - check
            #     check += 1
            # else:
            #     return -1
        return step
grid = [[0,0,1],[1,1,0],[1,0,0]]
grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
grid = [[1,0,0],[1,1,0],[1,1,1]]
grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
print(Solution().minSwaps(grid))