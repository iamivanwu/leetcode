class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0,1]
        if n < 2:
            return arr[n]
        index = 2
        while index <= n:
            m = index%2
            if m:
                arr.append(arr[index//2]+arr[index//2+1])
            else:
                arr.append(arr[index//2])
            index += 1
        return max(arr)
print(Solution().getMaximumGenerated(7))
