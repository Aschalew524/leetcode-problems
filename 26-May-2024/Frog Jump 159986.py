# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        memo = {}
        if n < 2 or stones[1] != 1:
            return False
        def dp(idx, last_jump):
            if (idx, last_jump) in memo:
                return memo[(idx, last_jump)]
            if idx == n - 1:
                return True

            choices = [last_jump - 1, last_jump, last_jump + 1]
            for jump in choices:
                if jump > 0:
                    next = stones[idx] + jump
                    if next in stones:
                        next_idx = stones.index(next)
                        if dp(next_idx, jump):
                            memo[(idx, last_jump)] = True
                            return True

            memo[(idx, last_jump)] = False
            return False

        return dp(1, 1)