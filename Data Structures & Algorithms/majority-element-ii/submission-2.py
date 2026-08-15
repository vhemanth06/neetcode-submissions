class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1=can2=-1
        ct1=ct2=0
        for num in nums:
            if num==can1:
                ct1+=1
            elif num==can2:
                ct2+=1
            elif ct1==0:
                ct1=1
                can1=num
            elif ct2==0:
                ct2=1
                can2=num
            else:
                ct1-=1
                ct2-=1
        ct1=ct2=0
        for num in nums:
            if can1==num:
                ct1+=1
            if can2==num:
                ct2+=1
        res=[]
        if ct1>len(nums)//3:
            res.append(can1)
        if ct2>len(nums)//3:
            res.append(can2)
        return res