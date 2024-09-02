# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return [] 
        ans = [[0] * n for _ in range(m)]  
        x = 0
        for i in range(m):
            for j in range(n):
                ans[i][j] = original[x]
                x += 1
        return ans