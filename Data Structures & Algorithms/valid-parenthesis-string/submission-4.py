class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin=0

        leftmax=0
        for i,c in enumerate(s):
            # print(f"{i}[{c}]->{leftmin} to {leftmax}")
            if c=='(':
                leftmin+=1
                leftmax+=1
            elif c==')':
                leftmin-=1
                leftmax-=1
                leftmin=max(0,leftmin)
                if leftmax<0:
                    return False
                # leftmax=max(0,leftmax)
            else:
                leftmin-=1
                leftmax+=1
                leftmin=max(0,leftmin)
        
        return leftmin==0
        # return leftmin*leftmax<=0