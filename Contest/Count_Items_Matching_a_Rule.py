from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule = ['type','color','name'].index(ruleKey)
        res = 0
        for item in items:
            if item[rule] == ruleValue:
                res += 1
        return res