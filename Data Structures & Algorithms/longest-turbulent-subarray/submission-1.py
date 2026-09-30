class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        if len(arr)==2:
            if arr[0]==arr[1]:
                return 1
            else:
                return 2
        camp=[]
        n=len(arr)
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                camp.append("<")
            elif arr[i]<arr[i-1]:
                camp.append(">")
            else:
                camp.append("=")
        maxlen=0
        if camp[0]!="=":
            prev=camp[0]
            i=1
        else:
            i=0
            while i<len(camp) and camp[i]=="=":
                i+=1
            if i>=len(camp):
                return 1
            prev=camp[i]
            i+=1
        
        temp=1
        while i<len(camp):
            if camp[i]!=prev and camp[i]!="=":
                prev=camp[i]
                temp+=1
                
                # continue
            elif camp[i]=="=":
                # print(i)
                maxlen=max(temp,maxlen)
                while i<len(camp) and camp[i]=="=":
                    i+=1
                if i>=len(camp):
                    break
                temp=1
                prev=camp[i]
                # i+=1
            else:
            # if camp[i]==prev:
                maxlen=max(temp,maxlen)
                print(i)
                temp=1
                prev=camp[i]
            i+=1
        # print(i)
        maxlen=max(temp,maxlen)
        return maxlen+1
                

