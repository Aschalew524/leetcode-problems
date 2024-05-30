# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        memo = {}

        def dp(idx1, mask):
            if (idx1, mask) in memo:
                return memo[(idx1, mask)]
            if idx1 == n:
                return 0
            min_xor = float('inf')
            for i in range(n):
                if mask & (1 << i) == 0:
                    min_xor = min(min_xor, (nums1[idx1] ^ nums2[i]) + dp(idx1 + 1, mask | (1 << i)))
            memo[(idx1, mask)] = min_xor
            return min_xor

        return dp(0, 0)