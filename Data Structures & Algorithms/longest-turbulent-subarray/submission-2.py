class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        inc=1
        dec=1
        n=len(arr)
        maxlen=1
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                inc=1+dec
                dec=1
            elif arr[i]<arr[i-1]:
                dec=1+inc
                inc=1
            else:
                dec=1
                inc=1
            maxlen=max(maxlen,inc,dec)
        return maxlen
            