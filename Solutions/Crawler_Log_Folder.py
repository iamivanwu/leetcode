from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        init = 0
        for log in logs:
            pre = log.split('/')[0]
            if pre == '..':
                if init > 0:
                    init -= 1
            elif pre == '.':
                continue
            else:
                init += 1
        return init