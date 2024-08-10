# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    remainders = [[0, 3], [1, 2]]

    def reachNumber(self, target: int) -> int:
        l, r = 0, abs(target)

        while l <= r:
            mid = floor(l + (r - l) / 2)
            sum = mid * (mid + 1) / 2

            if -sum <= target <= sum:
                r = mid - 1
            else:
                l = mid + 1

        while l % 4 not in self.remainders[target % 2]:
            l += 1

        return l