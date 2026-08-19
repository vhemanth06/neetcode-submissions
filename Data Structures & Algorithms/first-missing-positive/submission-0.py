class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        x=float('inf')
        for num in nums:
            if num>0:
                x=min(x,num)
        if x>1:
            return 1
        s=set(nums)
        res=0
        while res==0:
            x+=1
            if x not in s:
                res=x
        return res
