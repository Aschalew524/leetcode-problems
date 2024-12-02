# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(lis, idx):
            if len(lis) >= 2 and lis not in res:
                res.append(lis[:])  
            for i in range(idx, n):
                if not lis:
                    dfs(lis + [nums[i]], i + 1)
                elif nums[i] >= lis[-1]:
                    dfs(lis + [nums[i]], i + 1)
                
        dfs([], 0)
        return res