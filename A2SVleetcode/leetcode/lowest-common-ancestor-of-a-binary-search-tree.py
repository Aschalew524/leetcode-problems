# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, p, q):
            if node is None:
                return None
            
            
            if node.val  > p.val and node.val > q.val:
                return dfs(node.left, p, q)
            
            
            elif node.val < p.val and node.val < q.val:
                return dfs(node.right, p, q)

            else:
                return node
        return dfs(root, p, q)

