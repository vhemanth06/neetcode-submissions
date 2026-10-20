class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        cache={}
        def dp(i,Alice):
            if i==n:
                return 0
            if (i,Alice) in cache:
                return cache[(i,Alice)]
            score=0
            res=-float('inf') if Alice else float('inf')
            for j in range(i,min(i+3,n)):
                if Alice:
                    score+=stoneValue[j]
                    res=max(res,score+dp(j+1,not Alice))
                else:
                    score-=stoneValue[j]
                    res=min(res,score+dp(j+1,not Alice))
            cache[(i,Alice)]=res
            return res
        
        result=dp(0,True)
        if result==0:
            return "Tie"
        elif result>0:
            return "Alice"
        else:
            return "Bob"