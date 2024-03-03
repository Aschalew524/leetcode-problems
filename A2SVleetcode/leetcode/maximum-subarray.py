class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = 0
        curr_sum = 0
        max_sum = -float('inf')
        for r in range(len(nums)):
            curr_sum += nums[r]

            while (curr_sum <= 0 or nums[l] <= 0) and l < r:
                curr_sum -= nums[l]
                l += 1

            max_sum = max(curr_sum, max_sum)

        return max_sum

