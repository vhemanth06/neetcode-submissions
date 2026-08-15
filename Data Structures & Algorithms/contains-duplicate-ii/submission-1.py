class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        m=set()
        for r in range(len(nums)):
            if (r-l)>k:
                m.remove(nums[l])
                l+=1
            if nums[r] in m:
                return True
            m.add(nums[r])
        return False