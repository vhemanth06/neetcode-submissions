class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=[0]*(len(nums)+1)
        for num in nums:
            x[num]+=1
        for i in range(len(nums)+1):
            if x[i]==0:
                return i
                