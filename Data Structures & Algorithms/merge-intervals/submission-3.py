class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        temp=intervals[0]   
        for i in range(1,len(intervals)):
            if temp[1]<intervals[i][0]:
                res.append(temp)
                temp=intervals[i]
            elif temp[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                temp=[
                    min(intervals[i][0],temp[0]),
                    max(intervals[i][1],temp[1])
                ]
        res.append(temp)
        return res