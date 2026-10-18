class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        side=sum(nums)//k
        nums.sort(reverse=True)
        n=len(nums)
        used=[False]*n
        def dfs(i,k,subsum):
            if k==0:
                return True
            if subsum==side:
                return dfs(0,k-1,0)
            for j in range(i,n):
                if used[j] or subsum+nums[j]>side:
                    continue
                used[j]=True
                if dfs(j+1,k,subsum+nums[j]):
                    return True
                used[j]=False
            return False
        return dfs(0,k,0)
            