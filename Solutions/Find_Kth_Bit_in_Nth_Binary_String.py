class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        l = len(s)
        while l < k:
            inv = ''
            for j in range(len(s)-1,-1,-1):
                if s[j] == '0':
                    inv += '1'
                else:
                    inv += '0'
            s = s + '1' + inv
            l = len(s)
        return s[k-1]