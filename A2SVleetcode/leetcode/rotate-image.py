class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        n = len(matrix)
        
        i = 0
        j = 0
        while i < n and j < n+1:
            if j != n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            else:
                i += 1
                j = i
                if j == n:
                    j += 1
        
        for k in range(n):
            matrix[k] = matrix[k][::-1]
        