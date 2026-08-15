from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=defaultdict(int)
        n=len(nums)
        nc=n//3
        res=set()
        for num in nums:
            x[num]+=1
            if x[num]>nc:
                res.add(num)
        return list(res)
