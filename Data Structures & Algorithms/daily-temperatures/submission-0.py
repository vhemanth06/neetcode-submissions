class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[]
        res=[0]*len(temperatures)
        for i,num in enumerate(temperatures):
            # x=True
            while s and s[-1][1]<num:
                x,y=s.pop()
                res[x]=i-x
            s.append([i,num])
        return res