# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)

        i = 0
        while i < n:
            correct_index = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
        """
        :type nums: List[int]
        :rtype: int
        """
        