class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo=defaultdict(int)
        for i in coins:
            memo[i]=1
        def dp(am):
            if am in memo:
                return memo[am]
            elif am==0:
                return 0
            elif am<0:
                return float('inf')
            res=float('inf')
            for i in coins:
                x=dp(am-i)
                if x != float('inf'):
                    res=min(res,1+x)
            memo[am]=res
            return memo[am]
        x=dp(amount)
        # print(memo)
        return x if x != float('inf') else -1
