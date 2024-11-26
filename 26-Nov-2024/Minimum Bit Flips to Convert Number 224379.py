# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bin_start = bin(start)[2:]
        bin_goal = bin(goal)[2:]
        max_len = max(len(bin_start), len(bin_goal))
        bin_start = bin_start.zfill(max_len)
        bin_goal = bin_goal.zfill(max_len)
        res = 0
        for start, goal in zip(bin_start, bin_goal):
            if start != goal:
                res += 1
        return res