class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        
        per=self.permute(nums[1:])
        res=[]
        for p in per:
            for i in range(len(p)+1):
                x=p.copy()
                x.insert(i,nums[0])
                res.append(x)
        return res
        