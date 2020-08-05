class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and 1010101010101010101010101010101 & num == num and num & (num-1) == 0