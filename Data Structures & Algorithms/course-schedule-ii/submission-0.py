class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for x,y in prerequisites:
            adj[x].append(y)
        visited=set()
        cycle=set()
        res=[]
        def dfs(i):
            
            if i in cycle:
                return False
            if i in visited:
                return True
            cycle.add(i)
            for x in adj[i]:
                if dfs(x)==False:
                    return False
            cycle.remove(i)
            visited.add(i)
            res.append(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res



        