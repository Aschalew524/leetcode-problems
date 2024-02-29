# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[]
        summ=0
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        for i in ans:
            if i >= low and i<=high:
                summ+=i
        return summ


        
        