# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position, m) :
        position.sort()
        l, r = 1, position[-1] - position[0]
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            lastPos, balls = position[0], 1
            for i in range(1, len(position)):
                if position[i] - lastPos >= mid:
                    lastPos = position[i]
                    balls += 1
            if balls >= m:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans