class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n=mountainArr.length()
        cache=defaultdict(int)
        #find peak
        peak=-1
        l,r=0,n-1
        while l<=r:
            m=(l+r)//2
            if m in cache:
                y=cache[m]
            else:
                y=mountainArr.get(m)
                cache[m]=y

            if m-1 in cache:
                x=cache[m-1]
            else:
                x=mountainArr.get(m-1)
                cache[m-1]=x
            
            if m+1 in cache:
                z=cache[m+1]
            else:
                z=mountainArr.get(m+1)
                cache[m+1]=z
            
            # x,y,z=mountainArr.get(m-1),,mountainArr.get(m+1)
            if x<y<z:
                l=m+1
            elif x>y>z:
                r=m-1
            else:
                peak=m
                break
        
        #checkleft
        l,r=0,peak
        while l<=r:
            m=(l+r)//2
            if m in cache:
                x=cache[m]
            else:
                x=mountainArr.get(m)
                cache[m]=x
            if target<x:
                r=m-1
            elif target >x:
                l=m+1
            else:
                return m
        
        #checkright
        l,r=peak,n-1
        while l<=r:
            m=(l+r)//2
            if m in cache:
                x=cache[m]
            else:
                x=mountainArr.get(m)
                cache[m]=x
            if target<x:
                l=m+1
            elif target>x:
                r=m-1
            else:
                return m
        
        return -1
        
            