class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashmap=defaultdict(list)
        uniqueq=[]
        for i,q in enumerate(queries):
            if q not in hashmap:
                uniqueq.append(q)
            hashmap[q].append(i)
        minheap=[]
        res=[-1]*len(queries)
        uniqueq.sort()
        # queries.sort()
        intervals.sort()
        i=0
        n=len(intervals)
        
        for q in uniqueq:
            while i<n and q>=intervals[i][0]:
                heapq.heappush(minheap,[intervals[i][1]-intervals[i][0]+1,intervals[i][1]])
                i+=1
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            if minheap:
                for j in hashmap[q]:

                    res[j]=minheap[0][0]
        return res