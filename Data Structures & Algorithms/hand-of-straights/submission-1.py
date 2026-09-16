class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count={}
        for num in hand:
            count[num]=1+count.get(num,0)
        
        minh=list(count.keys())
        heapq.heapify(minh)
        # print(count)
        while minh:

            n=minh[0]
            # print(n)
            if count[n]==0:
                heapq.heappop(minh)
                continue
            for i in range(n,n+groupSize):
                if i not in count or count[i]==0:
                    return False
                count[i]-=1
            # print(count)
        return True

