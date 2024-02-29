# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       
        def check(Left_node , right_node):
            if Left_node  == None and right_node == None:
                return True
            if not Left_node or not right_node  or Left_node.val != right_node.val:
                return False
            return check(Left_node.left,right_node.right) and check(Left_node.right,right_node.left)
        return check(root , root)