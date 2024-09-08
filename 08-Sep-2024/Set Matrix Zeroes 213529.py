# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        dict={'row':[],'column':[]}
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])):
                if matrix[i][j]==0: 
                    dict['row'].append(i)
                    dict['column'].append(j)
        for i in dict["row"]: 
            for j in range(len(matrix[0])): 
                matrix[i][j]=0
        for i in dict["column"]:
            for j in range(len(matrix)): 
                matrix[j][i]=0