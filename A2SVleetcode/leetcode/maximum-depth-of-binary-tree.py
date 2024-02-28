# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxx(node):
            if node is None:
                return 0
            else:
                maxleft=0
                maxright=0
                if node.left:
                    maxleft=maxx(node.left)
                if node.right:
                    maxright=maxx(node.right)
            return max(maxleft,maxright)+1
        return maxx(root)




        