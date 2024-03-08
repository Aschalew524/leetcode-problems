# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def summ(node,s):
            if node.left is None and node.right is None:
                s += str(node.val)
                return int(s)
            s += str(node.val)

            l, r = 0, 0
            if node.left:
                l = summ(node.left, s)
            if node.right:
                r = summ(node.right, s)
            return l + r
        return   summ(root,"")

                    
                
        