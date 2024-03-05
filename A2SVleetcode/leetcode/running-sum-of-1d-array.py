class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        total=0
        for r in nums:
            total+=r
            res.append(total)
        return res