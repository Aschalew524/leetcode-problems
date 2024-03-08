class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l=0
        max_=0
        for r in range(len(nums)):
            if(nums[r]==0):
               k-=1
            while(k<0):
                k+=1-nums[l]
                l+=1
            max_=max(max_,r-l+1)
        return max_