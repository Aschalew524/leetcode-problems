# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]
        for k in range(2 , n):
            for i in range(n - k):
                start , end = i , i + k
                dp[start][end] = float("inf")
                for j in range(start + 1 , end):
                    dp[start][end] = min(dp[start][end] , dp[start][j] + dp[j][end] + A[start] * A[end] * A[j])
        return dp[0][-1]