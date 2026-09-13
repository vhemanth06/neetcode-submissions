class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        cache={}
        def dp(i,s):
            if (i,s) in cache:
                return cache[(i,s)]
            if i==n:
                if s==target:
                    cache[(i,s)]=1
                    # return 1
                else:
                    cache[(i,s)]=0
                return cache[(i,s)]
            
            cache[(i,s)]=dp(i+1,s+nums[i])+dp(i+1,s-nums[i])
            return cache[(i,s)]
        return dp(0,0)