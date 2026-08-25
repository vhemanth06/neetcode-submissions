class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n=len(a),len(b)
        i,j=m-1,n-1
        s=''
        carry=0
        while i>=0 and j>=0:
            if a[i]=='1' and b[j]=='1' and carry==1:
                s='1'+s
                carry=1
            elif (a[i]=='0' and b[j]=='1' and carry==1) or (a[i]=='1' and b[j]=='0' and carry==1) or (a[i]=='1' and b[j]=='1' and carry==0):
                s='0'+s
                carry=1
            elif (a[i]=='0' and b[j]=='0' and carry==1) or (a[i]=='0' and b[j]=='1' and carry==0) or (a[i]=='1' and b[j]=='0' and carry==0):
                s='1'+s
                carry=0
            elif a[i]=='0' and b[j]=='0' and carry==0:
                s='0'+s
                carry=0
            i-=1
            j-=1
        while i>=0:
            if a[i]=='1'  and carry==1:
                s='0'+s
                carry=1
            elif (a[i]=='0' and carry==1) or (a[i]=='1' and carry==0):
                s='1'+s
                carry=0
            elif a[i]=='0'and carry==0:
                s='0'+s
                carry=0
            i-=1
        while j>=0:
            if b[j]=='1'  and carry==1:
                s='0'+s
                carry=1
            elif (b[j]=='0' and carry==1) or (b[j]=='1' and carry==0):
                s='1'+s
                carry=0
            elif b[j]=='0'and carry==0:
                s='0'+s
                carry=0
            j-=1
        if carry==1:
            s="1"+s
        return s

        
