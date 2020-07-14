from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i],carry = (digits[i] + carry) % 10, (digits[i] + carry) // 10
        if carry:
            digits = [carry] + digits
        return digits
print(Solution().plusOne([9]))