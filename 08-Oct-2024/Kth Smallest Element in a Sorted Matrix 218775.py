# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        check=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                check.append(matrix[i][j])
        check.sort()
        return check[k-1]