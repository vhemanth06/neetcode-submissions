class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        res=r
        n=len(weights)
        while l<=r:
            m=(l+r)//2
            # i=0
            s=0
            d=1
            for w in weights:
                if s+w>m:
                    d+=1
                    s=w
                else:
                    s+=w
            # print(d)
            # print(m)
            if d<=days:
                res=min(m,res)
                r=m-1
            else:
                l=m+1
        return res




