# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        rem = k % s
        i = 0
        while rem > 0 and i < len(chalk):
            rem -= chalk[i]
            if rem < 0:
                return i
            i += 1
        return i
            