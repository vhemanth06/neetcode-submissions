class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        candidates.sort()
        subset=[]
        res=[]
        def dfs(i,s):
            if s==target:
                res.append(subset.copy())
                return
            elif s>target or i>=n:
                return
            subset.append(candidates[i])
            dfs(i+1,s+candidates[i])
            subset.pop()
            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,s)
        dfs(0,0)
        return res

            