import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x=[]
        n=len(nums)
        for num in nums:
            heapq.heappush(x,num)
            if len(x)>k:
                heapq.heappop(x)
            # print(x)
        return x[0]