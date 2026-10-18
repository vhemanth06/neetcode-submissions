class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        peri=sum(matchsticks)
        print(peri)
        if peri%4!=0:
            return False
        side=peri//4
        if max(matchsticks)>side:
            return False
        n=len(matchsticks)
        sides=[0]*4
        def dfs(i):
            # if l>side or t>side or r>side or b>side:
            #     return False
            if i==n:
                return True
            # if i>=n:
            #     return False
            for s in range(4):
                if sides[s]+matchsticks[i]<=side:
                    sides[s]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[s]-=matchsticks[i]
            return False
                
        return dfs(0)


        
        