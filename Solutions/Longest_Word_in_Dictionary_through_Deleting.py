from typing import List
import collections
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ret,l = '',-1
        for word in d:
            i,j = 0,0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                if len(word) > l or (len(word) == l and word < ret):
                    ret = word
                    l = len(word)
        return ret
