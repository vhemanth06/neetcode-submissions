class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s=[]
        maxarea=0
        n=len(heights)
        for i,num in enumerate(heights):
            if not s:
                s.append([i,heights[i]])
            else:
                y=0
                x=i
                while s and s[-1][1]>heights[i]:
                    x,y=s.pop()
                    maxarea=max(maxarea,y*(i-x))
                if not s or s[-1][1]!=heights[i]:
                    s.append([x,heights[i]])
            # print(f"{maxarea} s={s}")
        while s:
            x,y=s.pop()
            maxarea=max(maxarea,y*(n-x))
        return maxarea

                    
