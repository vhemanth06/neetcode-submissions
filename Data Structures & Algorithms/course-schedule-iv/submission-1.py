class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for x,y in prerequisites:
            adj[y].append(x)
        premap={}
        def dfs(i):
            if i not in premap:
                premap[i]=set()
                for c in adj[i]:
                    premap[i] |=dfs(c)
                premap[i].add(i)
            return premap[i]
            

        for c in range(numCourses):
            dfs(c)
        # target=-1
        # cycle=set()
        # visited=set()
        
        res=[]
        for x,y in queries:
            res.append(x in premap[y])

            # res.append(dfs(x,y,set()))
        return res
