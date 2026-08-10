class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=nums.copy()
        l=len(nums)
        for num in nums:
            x.append(num)
        return x
        