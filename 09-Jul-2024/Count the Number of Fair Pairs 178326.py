# Problem: Count the Number of Fair Pairs - https://leetcode.com/problems/count-the-number-of-fair-pairs/description/

class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        right = len(nums) - 1
        count = 0
        while right > 0:
            start = bisect.bisect_left(nums, lower - nums[right], 0, right)
            end = bisect.bisect_right(nums, upper - nums[right], 0, right) - 1
            if end >= start:
                count += end - start + 1
            right -= 1
        return count