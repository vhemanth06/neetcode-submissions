from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m=defaultdict(int)
        n=len(numbers)
        res=[-1,-1]
        for i in range(n):
            x=target-numbers[i]
            if x in m:
                return [m[x]+1,i+1]
            else:
                m[numbers[i]]=i
        