class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        n=len(nums)
        p,s=1,1
        for i in range(n):
            p=p*nums[i]
            s=s*nums[n-i-1]
            res=max(res,max(p,s))
            if nums[i]==0:
                p=1
            if nums[n-i-1]==0:
                s=1
            
        return res