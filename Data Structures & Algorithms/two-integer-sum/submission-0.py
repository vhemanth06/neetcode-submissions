class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        l=len(nums)
        for i in range(l):
            ex=target-nums[i]
            if ex in m:
                return sorted([m[ex],i])
            else:
                m[nums[i]]=i
            

        