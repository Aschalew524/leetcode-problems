class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead."""
        l = 0
        r = len(s) - 1
        while l < r:
            a=s[l]
            s[l],s[r] = s[r],a
            l += 1
            r -= 1

       
        