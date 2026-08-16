class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        if k==0:
            return
        def reverse(x,l,r):
            while l<r:
                x[l],x[r]=x[r],x[l]
                l+=1
                r-=1
        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)
