class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        x={
            'a':1,
            'b':1,
            'l':2,
            'n':1,
            'o':2
        }
        y={
            'a':0,
            'b':0,
            'l':0,
            'n':0,
            'o':0
        }
        for i in text:
            if i in y:
                y[i]+=1
        a=y['a']/x['a']
        b=min(a,y['b']/x['b'])
        l=min(b,y['l']/x['l'])
        n=min(l,y['n']/x['n'])
        o=min(n,y['o']/x['o'])
        return int(o)