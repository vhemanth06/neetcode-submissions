class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        su=sum(stones)
        half=su//2
        mindiff=half
        res=-1
        n=len(stones)
        cache={}
        def dfs(i,s):
            if i==n or s>=half:
                return abs(2*s-su)
            if (i,s) in cache:
                return cache[(i,s)]
            cache[(i,s)]=min(dfs(i+1,s),dfs(i+1,s+stones[i]))
            return cache[(i,s)]
            
        return dfs(0,0)
            
