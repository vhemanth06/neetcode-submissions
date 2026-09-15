class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax=0
        globalmax=nums[0]
        curmin=0
        globalmin=nums[0]
        s=0
        for num in nums:
            curmax=max(num,num+curmax)
            globalmax=max(globalmax,curmax)
            curmin=min(num,num+curmin)
            globalmin=min(globalmin,curmin)
            s+=num
        return max(globalmax,s-globalmin) if globalmax>=0 else globalmax