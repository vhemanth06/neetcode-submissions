from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m=defaultdict(list)
        for i in strs:
            x=tuple(sorted(i))
            m[x].append(i)
        return list(m.values())

        