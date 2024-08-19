# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = 0
        def dfs(node, sum):
            if node:
                if node.left is None and node.right is None:
                    if sum + node.val == targetSum:
                        return True
                if dfs(node.left, sum+node.val):
                    return True
                if dfs(node.right, sum+node.val):
                    return True
        return dfs(root, 0)
                
                    