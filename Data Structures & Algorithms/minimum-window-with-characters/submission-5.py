class Solution:
    def minWindow(self, s: str, t: str) -> str:
        map1=defaultdict(int)
        for c in t:
            map1[c]+=1
        
        l=0
        n=len(s)
        need=len(map1)
        have=0
        map2=defaultdict(int)
        res=[-1,-1]
        reslen=float('inf')
        for i in range(len(s)):
            if s[i] in map1:
                map2[s[i]]+=1
                if map2[s[i]]==map1[s[i]]:
                    have+=1
                while have==need:
                    while s[l] not in map1:
                        l+=1
                    # temp=[l,i]
                    if i-l+1<reslen:
                        res=[l,i]
                        reslen=i-l+1
                    map2[s[l]]-=1
                    if s[l] in map1 and map2[s[l]]<map1[s[l]]:
                        have-=1
                    l+=1
        l,r=res
        return s[l:r+1] if reslen!=float('inf') else ''

