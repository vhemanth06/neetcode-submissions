class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def bt(perm,pick):
            if len(perm)==n:
                res.append(perm[:])
                return
            for i in range(n):
                if pick[i]:
                    continue
                if i and nums[i]==nums[i-1] and not pick[i-1]:
                    continue
                
                perm.append(nums[i])
                pick[i]=True
                bt(perm,pick)
                perm.pop()
                pick[i]=False
        nums.sort()
        bt([],[False]*n)
        return res
            


            