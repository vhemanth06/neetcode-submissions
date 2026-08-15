class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def b(l,r):
            if l>r:
                return -1
            m=(l+r)//2
            if target<nums[m]:
                return b(l,m-1)
            elif target>nums[m]:
                return b(m+1,r)
            else:
                return m
        return b(0,len(nums)-1)