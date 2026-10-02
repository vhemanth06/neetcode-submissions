class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(openn,closen,s):
            if openn==closen==n:
                res.append(s)
                return
            if openn<n:
                dfs(openn+1,closen,s+"(")
            if closen<openn:
                dfs(openn,closen+1,s+")")
        dfs(0,0,"")
        return res
        
        