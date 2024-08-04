# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n & n-1 or n==0:
            return 0
        return 1
        