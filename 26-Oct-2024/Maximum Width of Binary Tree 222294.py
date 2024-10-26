# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def bfs(root):
            queue = deque([(root, 0)])
            max_width = 0
            
            while queue:
                n = len(queue)
                _, first_idx = queue[0]
                last_idx = first_idx
                
                for i in range(n):
                    node, idx = queue.popleft()
                    last_idx = idx
                    
                    if node.left:
                        queue.append((node.left, 2 * idx))
                    if node.right:
                        queue.append((node.right, 2 * idx + 1))
                
                max_width = max(max_width, last_idx - first_idx + 1)
            
            return max_width
        
        return bfs(root)





        
        