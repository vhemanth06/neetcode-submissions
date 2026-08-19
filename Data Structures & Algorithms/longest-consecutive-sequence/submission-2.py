class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums :
            return 0
        x=set(nums)
        res=1
        for num in nums:
            if num-1 not in x:
                i=1
                while num+i in x:
                    i+=1
                res=max(res,i)
            else:
                continue
        return res