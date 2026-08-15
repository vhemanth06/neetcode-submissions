class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        if l==1:
            return 0
        p1=0
        p2=1
        r=0
        while p1<l and p2<l:
            if prices[p2]<prices[p1]:
                p1+=1
                continue
            r=max(r,prices[p2]-prices[p1])
            p2+=1
        return r
        