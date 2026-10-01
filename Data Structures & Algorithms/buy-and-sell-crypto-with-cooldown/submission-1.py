class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        cache={}
        def dp(i,holding):
            if i>=n:
                return 0
            if (i,holding) in cache:
                return cache[(i,holding)]
            if holding:
                x=prices[i]+dp(i+2,False)
            else:
                x=-prices[i]+dp(i+1,True)
            skip=dp(i+1,holding)
            res=max(x,skip)
            cache[(i,holding)]=res
            return res
        return dp(0,False)
        # return