# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def build(nums):
            if len(nums)==0:
                return 
            m=max(nums)
            i=nums.index(m)
              
            root=TreeNode(nums[i])
            root.left=build(nums[:i])
            root.right=build(nums[i+1:])
            return root
        return build(nums)
            
        

        