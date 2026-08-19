from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s=0
        res=0
        prefix=[]
        for num in nums:
            s+=num
            if s==k:
                res+=1
            prefix.append(s)
        print(prefix)
        x=defaultdict(int)
        
        for p in prefix:
            target=p-k
            if target in x:
                res+=x[target]
            
            x[p]+=1
        print(x)
        return res