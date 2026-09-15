class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        prefix=[0]*(n+1)
        minus=0
        for i in range(1,n+1):
            if nums[i-1]<0:
                minus+=1
            prefix[i]=nums[i-1]+prefix[i-1]
        # print(prefix)
        if minus==n:
            return max(nums)
        res=0
        m=10001
        for i in range(len(prefix)):
            m=min(m,prefix[i])
            res=max(res,prefix[i]-m)
        
        return res