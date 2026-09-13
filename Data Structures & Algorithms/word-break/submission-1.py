class Solution:
    def wordBreak(self, word: str, wordDict: List[str]) -> bool:
        hash1=set(wordDict)
        n=len(word)
        memo={}
        def dp(i,s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i==n:
                if s in hash1:
                    memo[(i,s)]=True
                    # return True
                else:
                    memo[(i,s)]=False
                return memo[(i,s)]
            x=s+word[i]
            # res=True
            if (x in hash1) :
                memo[(i,s)]=dp(i+1,"") or dp(i+1,x)
            else:
                memo[(i,s)]= dp(i+1,x)
            return memo[(i,s)]
        return dp(0,"")

