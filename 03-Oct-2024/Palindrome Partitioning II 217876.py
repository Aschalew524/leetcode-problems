# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i-1 for i in range(n+1)]
        for i in range(n+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i]=min(dp[i],dp[j]+1)
        return dp[n]  