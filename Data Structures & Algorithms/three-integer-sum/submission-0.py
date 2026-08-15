class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        # print(nums)
        res=set()
        for i in range(n-2):
            l=i+1
            r=n-1
            x=0-nums[i]
            while l<r:
                if nums[l]+nums[r]<x:
                    l+=1
                elif nums[l]+nums[r]>x:
                    r-=1
                else:
                    res.add(tuple(sorted([nums[i],nums[l],nums[r]])))
                    l+=1
                    r-=1
        return [list(x) for x in res]
        