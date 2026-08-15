class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=0
        for i in range(1,len(prices)):
            d=prices[i]-prices[i-1]
            if d>0:
                x+=d
        return x