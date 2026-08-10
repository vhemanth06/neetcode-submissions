class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        # p1=0
        p=1
        k=0
        for i in range(1,l):
            if nums[i-1]==nums[i]:
                k+=1
                continue
            nums[p]=nums[i]
            p+=1
        return l-k

        