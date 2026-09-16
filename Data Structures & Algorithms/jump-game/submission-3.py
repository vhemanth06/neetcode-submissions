class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        cache={}
        def dp(i):
            if i>=n-1:
                return True
            if nums[i]==0:
                return False
            if i in cache:
                return cache[i]
            res=False
            for j in range(1,nums[i]+1):
                res=res or dp(i+j)
                if res:
                    cache[i]=True
                    return True
            cache[i]=False
            return False
        return dp(0)
