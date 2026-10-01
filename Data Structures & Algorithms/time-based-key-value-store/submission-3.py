class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)
        self.times=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append(value)
        self.times[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times or self.times[key][0]>timestamp:
            return ""
        if self.times[key][-1]<=timestamp:
            return self.hashmap[key][-1]
        l,r=0,len(self.times[key])-1
        while l<=r:
            m=(l+r)//2
            if self.times[key][m]<timestamp:
                l=m+1
            elif self.times[key][m]>timestamp:
                r=m-1
            else:
                return self.hashmap[key][m]
        return self.hashmap[key][r]