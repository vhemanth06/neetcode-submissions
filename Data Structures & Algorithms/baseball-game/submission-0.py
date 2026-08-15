class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        l=len(operations)
        for i in range(l):
            if operations[i]=='+':
                s.append(s[-1]+s[-2])
            elif operations[i]=='D':
                x=s[-1]
                s.append(2*x)
            elif operations[i]=='C':
                s.pop()
            else:
                s.append(int(operations[i]))
        
        # t=0
        # for num in s:
        #     t+=num
        return sum(s)

        