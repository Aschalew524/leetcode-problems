# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node):
            if not node:
                return None
            if node.val == startValue or node.val == destValue:
                return node
            
            left = lca(node.left)
            right = lca(node.right)
            
            if left and right:
                return node
            return left if left else right

        def dfs(node, target):
            if not node:
                return None
            if node.val == target:
                return ""
            
            left_path = dfs(node.left, target)
            if left_path is not None:
                return "L" + left_path
            
            right_path = dfs(node.right, target)
            if right_path is not None:
                return "R" + right_path
            
            return None
        
        lca = lca(root)
        
        path_to_start = dfs(lca, startValue)
        path_to_dest = dfs(lca, destValue)
        
        return "U" * len(path_to_start) + path_to_dest