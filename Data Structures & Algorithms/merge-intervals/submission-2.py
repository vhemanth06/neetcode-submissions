class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        temp=intervals[0]
        print(intervals)
        n=len(intervals)
        def isover(inter1,inter2):
            if inter1[1]>=inter2[0] or inter2[1]>=inter1[0]:
                return True
            else:
                return False
            
        for i in range(1,len(intervals)):
            # print(temp)
            if temp[1]<intervals[i][0]:
                res.append(temp)
                temp=intervals[i]
                # print(res+intervals[i:])
                # if i+1<n:
                #     # if isover(intervals[i+1],temp):

                #     #     temp=[
                #     #     min(intervals[i+1][0],temp[0]),
                #     #     max(intervals[i+1][1],temp[1])
                #     #     ]
                #     # else:
                #     #     res.append(temp)
                #     #     temp=intervals[i+1]
                #     temp=intervals[i]
                # else:
                #     # res.append(temp)
                #     return res
                # return res+intervals[i:]
            elif temp[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                temp=[
                    min(intervals[i][0],temp[0]),
                    max(intervals[i][1],temp[1])
                ]
        res.append(temp)
        # print(res)
        return res