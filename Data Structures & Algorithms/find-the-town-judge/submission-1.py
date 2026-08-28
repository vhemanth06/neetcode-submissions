# from collections import defaultdict,deque
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        source=[0]*n
        target=[0]*n
        for x,y in trust:
            source[x-1]+=1
            target[y-1]+=1
        for i in range(n):
            if source[i]==0 and target[i]==n-1:
                return i+1
        return -1
