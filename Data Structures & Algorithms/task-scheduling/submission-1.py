class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for task in tasks:
            count[ord(task)-ord('A')]+=1
        heap=[]
        for x in count:
            if x!=0:
                heap.append(-x)
        heapq.heapify(heap)
        # print(heap)
        q=deque()
        t=0
        # print(f"{heap}  {q}")
        while heap or q:
            if not heap:
                t+=1
                if q[0][1]==t:
                    y,_=q.popleft()
                    heapq.heappush(heap,y)
                continue
            x=heapq.heappop(heap)
            t+=1
            x+=1
            if x!=0:
                q.append((x,t+n))
            if q and q[0][1]==t:
                y,_=q.popleft()
                heapq.heappush(heap,y)
            # print(f"{heap}  {q}")
        return t
