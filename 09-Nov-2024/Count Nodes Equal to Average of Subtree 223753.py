# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt=0
        
        def dfs(node):
            sum_=0
            nonlocal cnt
            
            if node is None:
                return(0,0)
            
            left_sum,left_cnt=dfs(node.left)
            right_sum,right_cnt = dfs(node.right)

            total_sum=left_sum + right_sum + node.val
            total_cnt=left_cnt + right_cnt + 1

            average = total_sum//total_cnt
            if average == node.val:
                cnt+=1
            return total_sum,total_cnt
        dfs(root)
        return cnt

        

