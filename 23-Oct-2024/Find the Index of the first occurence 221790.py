# Problem: Find the Index of the first occurence - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        l = 0
        
        while l <= n - m:
            r = 0
            while r < m and haystack[l + r] == needle[r]:
                r += 1
            if r == m:
                return l
            l += 1
        
        return -1