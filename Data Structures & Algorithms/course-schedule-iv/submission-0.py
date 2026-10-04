class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj=defaultdict(list)
        for x,y in prerequisites:
            adj[x].append(y)
        # target=-1
        # cycle=set()
        # visited=set()
        def dfs(i,target,visited):
            if i==target:
                return True
            if i in visited:
                return False
            visited.add(i)
            for x in adj[i]:
                if dfs(x,target,visited):
                    return True
            return False
        res=[]
        for x,y in queries:

            res.append(dfs(x,y,set()))
        return res
