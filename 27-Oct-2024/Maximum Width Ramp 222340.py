# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        mono_stack = []
        max_width = 0
        
        for i in range(len(nums)):
            if not mono_stack or nums[i] <=  nums[mono_stack[-1]]  :
                mono_stack.append(i)
        
        for j in range(len(nums) - 1, -1, -1):
            while mono_stack and nums[j] >= nums[mono_stack[-1]]:
                max_width = max(max_width, j - mono_stack.pop())
        
        return max_width