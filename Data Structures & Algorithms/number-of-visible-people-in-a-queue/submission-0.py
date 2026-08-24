class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        s=[]
        n=len(heights)
        res=[0]*n
        for i in range(n-1,-1,-1):
            # res[i]=len(s)
            print(s)
            
            while s and s[-1]<heights[i]:
                res[i]+=1
                s.pop()
            # if s and  s[-1]>heights[i]:
                
            #     res[i]=1
            if s:
                res[i]+=1
            s.append(heights[i])
        return res