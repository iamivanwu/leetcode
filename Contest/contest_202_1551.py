class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2:
            return int(2*(n//2)*(n//2+1)/2)
        else:
            return int((n//2)*(2*(n//2))/2)
print(Solution().minOperations(6))