class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=='0' or num2=='0':
            return '0'
        hashmap={
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9   
        }
        hashmap2={y:x for x,y in hashmap.items()}
        res=0

        for sy in num2[::]:
            y=hashmap[sy]
            res*=10
            res2=0
            for sx in num1[::]:
                x=hashmap[sx]
                res2*=10
                res2+=(x*y)
                
            res+=res2
        s=""
        # print(res)
        while res:
            x=res%10
            # print(x)
            s=hashmap2[x]+s
            res=res//10
            
        return s
            

        
        
        
        