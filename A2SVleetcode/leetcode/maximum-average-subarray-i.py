class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Maxsum=summ=sum(nums[:k])
        avg=float("-inf")
        for i in range(k,len(nums)):
            summ=summ+nums[i]-nums[i-k]
            Maxsum=max(summ,Maxsum)
            
        return float(Maxsum/k)