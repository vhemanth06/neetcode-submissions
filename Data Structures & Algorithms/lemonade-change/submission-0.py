class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        x={
            5:0,
            10:0,
            20:0
        }
        for bill in bills:
            if bill ==5:
                x[5]+=1
            elif bill==10:
                if x[5]>0:
                    x[5]-=1
                    x[10]+=1
                else:
                    return False
            else:
                if x[5]>=3:
                    x[5]-=3
                    x[20]+=1
                elif (x[5]>=1 and x[10]>=1):
                    x[5]-=1
                    x[10]-=1
                    x[20]+=1
                else:
                    return False
        return True


