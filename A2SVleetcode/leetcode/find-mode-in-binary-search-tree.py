# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans={}

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            ans[(node.val)]=ans.get(node.val,0)+1
            inorder(node.right)
        
        inorder(root)
        print(ans)
        max_=max(ans.values())
        a =  [i for i,v in ans.items() if v== max_]
        return a
        
        
    