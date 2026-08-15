class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        m=[0,0,0]
        l=len(nums)
        for num in nums:
            m[num]+=1
        i=0
        nums[0:m[0]]=[0]*m[0]
        nums[m[0]:m[1]+m[0]]=[1]*m[1]
        nums[m[1]+m[0]:l]=[2]*m[2]

        