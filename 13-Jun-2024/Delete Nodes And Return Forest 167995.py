# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        to_delete = set(to_delete)
        ans = []
        def dfs(node):
            
            if not node or not to_delete:
                return
            if node.val in to_delete:
                to_delete.remove(node.val)
                if node.left and node.left.val not in to_delete:
                    ans.append(node.left)
                if node.right and node.right.val not in to_delete:
                    ans.append(node.right)
            else:
                if node.left and node.left.val in to_delete:
                    dfs(node.left)
                    node.left = None
                if node.right and node.right.val in to_delete:
                    dfs(node.right)
                    node.right = None
            dfs(node.left)
            dfs(node.right)
        if root.val not in to_delete:
            ans.append(root)
        dfs(root)
        return ans