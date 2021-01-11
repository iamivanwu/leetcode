class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
            if not n % 3:
                n = n // 3
            else:
                return False
        return False