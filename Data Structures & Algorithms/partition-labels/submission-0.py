class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        hashmap1=[0]*26
        for c in s:
            hashmap1[ord(c)-ord('a')]+=1
        i,j=0,0
        res=[]
        x=set()

        while j<n:
            x.add(s[j])
            hashmap1[ord(s[j])-ord('a')]-=1
            if hashmap1[ord(s[j])-ord('a')]==0:
                x.remove(s[j])
            
            if not x:
                res.append(j-i+1)
                i=j+1
            j+=1
            
        return res
