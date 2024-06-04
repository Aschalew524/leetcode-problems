# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_ = 0
        l,r=0,0
        while r < len(nums):
            if nums[r] == 1:
                max_ = max(r-l+1,max_)
                r+=1
            else:
                r+=1
                l=r
        return max_
		
        """
        :type nums: List[int]
        :rtype: int
        """
        