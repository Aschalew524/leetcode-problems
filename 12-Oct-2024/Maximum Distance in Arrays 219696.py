# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution(object):
    def maxDistance(self, nums):
        n = len(nums)
        max_distance = 0
        min_val = nums[0][0] 
        max_val = nums[0][-1]
        for i in range(1, n):
            max_distance = max(max_distance, abs(max_val - nums[i][0]))
            max_distance = max(max_distance, abs(min_val - nums[i][-1]))

            min_val = min(min_val, nums[i][0])
            max_val = max(max_val, nums[i][-1])
        return max_distance