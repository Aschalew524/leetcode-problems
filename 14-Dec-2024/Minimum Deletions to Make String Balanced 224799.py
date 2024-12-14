# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
  
        end_a, end_b = 0,0 
        for val in s:
            if val == 'a':
                end_b += 1
            else:
                end_a, end_b = end_a+1, min(end_a, end_b)
        return min(end_a, end_b)