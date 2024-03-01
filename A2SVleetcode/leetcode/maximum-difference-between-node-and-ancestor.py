# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        minn=float("inf")
        maxx=float("-inf")
        max_=[]
        def diff(node,maxx,minn):
            
            
            if not node:
                return
            minn=min(node.val,minn)
            maxx=max(node.val,maxx)
            dif=abs(maxx-minn)
            
            max_.append(dif)
            
            if node.left:
                diff(node.left,maxx,minn)
            if node.right:
                diff(node.right,maxx,minn)
            return max(max_)
        return diff(root,maxx,minn)
        
            
            
            




            
            

        