class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        x=0
        for i in range(l):
            if nums[i]==val:
                nums[i]=101
                x+=1
        nums.sort()
        return l-x
        

        