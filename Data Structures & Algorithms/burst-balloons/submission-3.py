from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # n=len(nums)
        arr=[1]+nums+[1]
        # print(arr)
        n=len(arr)
        # cache=defaultdict(int)
        @cache
        def dp(L,R):
            if L>R:
                return 0
            # if (L,R) in cache:
            #     return cache[(L,R)]
            res=0
            for i in range(L,R+1):
                res=max(res,arr[L-1]*arr[i]*arr[R+1]+dp(i+1,R)+dp(L,i-1))
            # cache[(L,R)]=res
            return res
        return dp(1,len(arr)-2)