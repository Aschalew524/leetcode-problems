# Problem: Find Bottom Left Tree Value - https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        ans = []
        queue.append(root)
        while queue:
            cur_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                cur_level.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            if cur_level :
                ans.append(cur_level)
       
        return ans[-1][0]