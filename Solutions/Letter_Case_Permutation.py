from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        def create(now):
            if len(now) == len(S):
                res.append(now)
            else:
                if S[len(now)].isalpha():
                    create(now+S[len(now)].lower())
                    create(now+S[len(now)].upper())
                else:
                    create(now+S[len(now)])
        create('')
        return res