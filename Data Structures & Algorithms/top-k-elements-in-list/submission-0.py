from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        for num in nums:
            m[num]+=1
        f=[[] for _ in range(len(nums))]
        for x,y in m.items():
            f[y-1].append(x)
        # print(m)
        # print(f)
        res=[]
        for i in range(len(f)-1,-1,-1):
            if f[i]:
                res.extend(f[i])
            if len(res)>=k:
                break
        return res

        