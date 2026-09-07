class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo=defaultdict(int)
        n=len(coins)
        def dp(i,am):
            if am==0:
                return 1
            if i>=n or am<0:
                return 0
            elif (i,am) in memo:
                return memo[(i,am)]

            # res=0
            # if am-coins[i]>0:
            res=dp(i,am-coins[i])+dp(i+1,am)
            
            memo[(i,am)]=res
            return memo[(i,am)]
        res=dp(0,amount)
        # print(memo)
        return res