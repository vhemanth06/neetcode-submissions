class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        # res=0
        cache={n-1:0}
        def dfs(i):
            if i in cache:
                return cache[i]
            if nums[i]==0:
                return float('inf')
            x=float('inf')
            e=min(n-1,i+nums[i])
            for j in range(i+1,e+1):
                x=min(x,1+dfs(j))
            cache[i]=x
            return x
        return dfs(0)