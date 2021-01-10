from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for code in encoded:
            res.append(res[-1]^code)
        return res