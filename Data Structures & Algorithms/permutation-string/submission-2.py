class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1=[0]*26
        hashmap2=[0]*26
        # print(ord(s1[0])-ord('a'))
        m=len(s1)
        n=len(s2)
        if m>n:
            return False
        for i in range(m):
            hashmap1[ord(s1[i])-ord('a')]+=1
            hashmap2[ord(s2[i])-ord('a')]+=1
        if hashmap1==hashmap2:
                return True
        i=0
        for j in range(m,n):                
                hashmap2[ord(s2[j])-ord('a')]+=1
                hashmap2[ord(s2[i])-ord('a')]-=1
                i+=1
                # j+=1
                if hashmap1==hashmap2:
                    return True



        return False