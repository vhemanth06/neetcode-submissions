class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>=nums[l]:
                if target>nums[m]:
                    l=m+1
                elif target<nums[m] and target>=nums[l]:
                    r=m-1
                elif target<nums[m] and target<nums[l]:

                    l=m+1
                else:
                    return m
            else:
                if target<nums[m]:
                    r=m-1
                elif target>nums[m] and target>nums[r]:
                    r=m-1
                elif target>nums[m] and target<=nums[r]:
                    l=m+1
                else:
                    return m
        return -1
