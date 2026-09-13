class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset=set(wordDict)
        n=len(s)
        memo={n:True}
        def dp(i):
            if i in memo:
                return memo[i]
            if i==n:
                return True
            for j in range(i+1,n+1):
                if s[i:j] in wordset and dp(j):
                    memo[i]=True
                    return True
            memo[i]=False
            return False
        return dp(0)