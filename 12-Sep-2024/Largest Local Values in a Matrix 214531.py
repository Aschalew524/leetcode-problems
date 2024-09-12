# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = []
        
        for i in range(n-2):
            row = []
            for j in range(n-2):
                sub_mat = []
                for k in range(3):
                    sub_mat.append(grid[i+k][j:j+3])
                max_ = max([max(r) for r in sub_mat])
                row.append(max_)
            maxLocal.append(row)
        
        return maxLocal



        