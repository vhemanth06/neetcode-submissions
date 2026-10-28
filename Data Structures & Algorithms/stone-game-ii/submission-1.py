class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        cache={}
        def dfs(i,M,alice):
            if i>=n :
                return 0
            if (i,M,alice) in cache:
                return cache[(i,M,alice)]
            stone=0
            best=0 if alice else float('inf')
            for j in range(1,2*M+1):
                index=i+j-1
                if index>=n:
                    break 
                stone+=piles[index]
                
                if alice:
                    s=dfs(index+1,max(j,M),not alice)
                    best=max(best,s+stone)
                else:
                    s=dfs(index+1,max(j,M),not alice)
                    best=min(best,s)
            cache[(i,M,alice)]=best
            return best
        return dfs(0,1,True)
        # return self.res

