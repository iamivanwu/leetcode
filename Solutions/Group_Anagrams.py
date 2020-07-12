from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        table = {}
        out = []
        count = 0
        for s in strs:
            if table.get(tuple(sorted(s))) == None:
                table[tuple(sorted(s))] = count
                out.append([s])
                count += 1
            else:
                out[table.get(tuple(sorted(s)))].append(s)
        return out

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))