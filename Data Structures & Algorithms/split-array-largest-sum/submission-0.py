class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(mid):
            res=0
            subarray=1
            for n in nums:
                res+=n
                if res>mid:
                    subarray+=1
                    res=n
            return subarray<=k
        l,r=max(nums),sum(nums)
        res=r
        while l<=r:
            mid=(l+r)//2
            if cansplit(mid):
                res=mid
                r=mid-1
            else:
                l=mid+1
        
        return res
        