class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        pre=[1]*l
        pos=[1]*l
        for i in range(1,l):
            pre[i]=pre[i-1]*nums[i-1]
        for i in range(l-2,-1,-1):
            pos[i]=pos[i+1]*nums[i+1]
        for i in range(l):
            pre[i]=pre[i]*pos[i]
        return pre