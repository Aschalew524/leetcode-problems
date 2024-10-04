# Problem: Minimize Maximum Pair Sum in Array - https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_=float('-inf')
        l=0
        r=len(nums)-1
        while l < r:
            max_ = max(nums[l]+ nums[r],max_)
            l+=1
            r-=1
        return max_

        