class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets.sort()
        q1=deque(triplets)
        # print(q1)
        p=q=r=0
        while q1:
            x,y,z=q1.popleft()
            if x>target[0] or y>target[1] or z>target[2]:
                # print('flag2')
                continue
            
            p=max(p,x)
            q=max(q,y)
            r=max(r,z)
            # print(list([p,q,r]))
            if p==target[0] and q==target[1] and r==target[2]:
                # print('flag1')
                return True
            
        return False
       
        