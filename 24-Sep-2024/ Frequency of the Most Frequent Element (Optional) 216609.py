# Problem:  Frequency of the Most Frequent Element (Optional) - https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        l= 0
        max_ = 0
        op = 0
        
        for r in range(len(nums)):
            op += (nums[r] - nums[r - 1]) * (r - l)
            
            while op > k:
                op -= nums[r] - nums[l]
                l+= 1
            
            max_ = max(max_, r - l+ 1)
        
        return max_
