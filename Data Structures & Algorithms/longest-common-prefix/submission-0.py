class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        ml=201
        for i in range(len(strs)):
            ml=min(ml,len(strs[i]))
        for i in range(ml):
            x=strs[0][i]
            for j in range(1,len(strs)):
                if x!=strs[j][i]:
                    return res
            res+=(x)
        return res


        