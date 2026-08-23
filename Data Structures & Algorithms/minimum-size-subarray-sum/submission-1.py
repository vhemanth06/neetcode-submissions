class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target>sum(nums):
            return 0
        i,j=0,0
        n=len(nums)
        sum1=0
        res=float('inf')
        while j<n:
            # print(f"{nums[i:j]} == {sum1} (i=={i},j=={j})")
            while sum1>=target:
                res=min(res,j-i)
                sum1-=nums[i]
                i+=1
            sum1+=nums[j]
            j+=1
        while sum1>=target:
                res=min(res,j-i)
                sum1-=nums[i]
                i+=1
        return res


        