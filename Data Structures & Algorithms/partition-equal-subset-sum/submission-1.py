class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s %2==1:
            return False
        target=s//2
        n=len(nums)
        memo=[[-1]*(target+1) for _ in range(n+1)]
        def dp(i,target):
            if target==0:
                return True
            if i>=n or target<0:
                return False
            if memo[i][target]!=-1:
                return memo[i][target]

            
            memo[i][target]= dp(i+1,target) or dp(i+1,target-nums[i])
            return memo[i][target]
        return dp(0,target)
        