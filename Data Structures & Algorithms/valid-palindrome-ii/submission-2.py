class Solution:
    def validPalindrome(self, s: str) -> bool:
         def ispal(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
         l=0
         r=len(s)-1
         counter=0
         while l<r:
            # print(l)
            # print(r)
            
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return ispal(l+1,r) or ispal(l,r-1)
         return True

        
        