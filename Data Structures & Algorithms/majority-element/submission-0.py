from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x=defaultdict(int)
        l=len(nums)
        t=l//2
        for i in range(l):
            x[nums[i]]+=1
            if x[nums[i]]>t:
                return nums[i]


        