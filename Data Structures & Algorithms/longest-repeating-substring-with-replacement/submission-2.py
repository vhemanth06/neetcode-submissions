class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        l,r=0,0
        
        n=len(s)
        res=0
        while r<n:
            # print(f"{l},{r}")
            count[ord(s[r])-ord('A')]+=1
            winlen=r-l+1
            countmax=max(count)
            if winlen-countmax<=k:
                r+=1
                res=max(res,winlen)
            else:
                count[ord(s[l])-ord('A')]-=1
                count[ord(s[r])-ord('A')]-=1
                l+=1
        return res

