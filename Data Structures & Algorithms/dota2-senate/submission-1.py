class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R=deque()
        D=deque()
        n=len(senate)
        for i,c in enumerate(senate):
            if c=="R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            x=R.popleft()
            y=D.popleft()
            if x<y:
                
                R.append(x+n)
            else:
                D.append(y+n)
        return "Radiant" if R else "Dire"

