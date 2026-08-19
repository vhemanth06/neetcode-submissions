class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):

            if nums[i]<0:
                nums[i]=0
        for num in nums:
            x=abs(num)
            if x>0 and x<=n:
                if nums[x-1]!=0:
                    nums[x-1]=abs(nums[x-1])*-1
                else:
                    nums[x-1]=-(n+1)
        print(nums)
        for i in range(1,n+1):
            if nums[i-1]>=0:
                return i
        return n+1