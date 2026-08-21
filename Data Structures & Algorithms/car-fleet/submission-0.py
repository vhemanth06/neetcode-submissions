class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=[]
        combined=list(zip(position,speed))
        combined.sort(key=lambda x:-x[0])
        time=[]
        for x in combined:
            time.append((target-x[0])/x[1])
        # print(time)
        # print(pos)
        # print(spe)
        for x in time:
            # print(s)
            if not s:
                s.append(x)
            else:
                if x>s[-1]:
                    s.append(x)
        # print(s)
        return len(s)