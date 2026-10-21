class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadset=set(deadends)
        
        start='0000'
        if start in deadset:
            return -1
        q=deque()
        visit=set()
        q.append(start)
        visit.add(start)
        h=0
        while q:
            l=len(q)
            for _ in range(l):
                
                x=q.popleft()
                # print(x)
                for i in range(4):
                    y=int(x[i])
                    for move in [-1,1]:
                        ny=(y+move)%10
                        nx=x[:i]+str(ny)+x[i+1:]
                        if nx==target:
                            return h+1
                        if nx not in visit and nx not in deadset:
                            q.append(nx)
                            visit.add(nx)
                    
                    
            h+=1
        return -1
                    
