class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        def bt(perm,pick):
            if len(perm)==n:
                res.add(tuple(perm[:]))
                return
            for i in range(n):
                if not pick[i]:
                    perm.append(nums[i])
                    pick[i]=True
                    bt(perm,pick)
                    perm.pop()
                    pick[i]=False
        bt([],[False]*n)
        return [list(x) for x in res]
            


            