class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res=0
        n=len(nums)
        memo={}
        def dfs(t):
            if t<0:
                return 0
            if t==0:
                return 1
            if t in memo:
                return memo[t]
            memo[t]=0
            for num in nums:
                memo[t]+=dfs(t-num)
            return memo[t]
        return dfs(target)
   
