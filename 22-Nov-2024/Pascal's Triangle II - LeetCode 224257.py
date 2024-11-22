# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] * (rowIndex + 1)  

        for i in range(1, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                res[j] += res[j - 1]

        return res