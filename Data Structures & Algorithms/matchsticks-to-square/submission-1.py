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
        def dfs(i,l,t,r,b):
            if l>side or t>side or r>side or b>side:
                return False
            if l==side and t==side and r==side and b==side:
                return True
            if i>=n:
                return False
            return dfs(i+1,l+matchsticks[i],t,r,b) or dfs(i+1,l,t+matchsticks[i],r,b) or dfs(i+1,l,t,r+matchsticks[i],b) or dfs(i+1,l,t,r,b+matchsticks[i])
        return dfs(0,0,0,0,0)


        
        