class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        n=len(s)
        res=0
        k=set()
        t=''
        while r<n:
            # print(k)
            if s[r] in k:
                while l<r and s[r] in k:
                    k.remove(s[l])
                    l+=1
                # t=s[l:r+1]
            
            res=max(res,r-l+1)
            k.add(s[r])
            r+=1
        return res


