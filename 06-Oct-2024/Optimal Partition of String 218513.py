# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        l=0
        cnt=1
        for r in range(len(s)):
            if s[r] in s[l:r]:
                cnt+=1
                l=r
        return cnt
        