class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j=0,0
        m,n=len(word),len(abbr)
        while i<m and j<n:
            if abbr[j] == '0':
                    return False
            if word[i]==abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isdigit():
                s=''
                while j<n and abbr[j].isdigit():
                    s+=abbr[j]
                    j+=1
                x=int(s)
                i+=x
            else:
                return False
        return i==m and j==n
