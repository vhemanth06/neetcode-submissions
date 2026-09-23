class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newinterval[1]<intervals[i][0]:
                res.append(newinterval)
                return res+intervals[i:]
            elif newinterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newinterval=[
                    min(intervals[i][0],newinterval[0]),
                    max(intervals[i][1],newinterval[1])
                ]
        res.append(newinterval)
        return res
            
