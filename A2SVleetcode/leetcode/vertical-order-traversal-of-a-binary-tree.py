# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        check=defaultdict(list)
        def dfs(root,r,c):
            if root:
                check[c].append([r,root.val])
                dfs(root.left,r+1,c-1)
                dfs(root.right,r+1,c+1)
            return
        dfs(root,0,0)
        check = list(check.items())
        check.sort(key=lambda x:x[0])
        
        for i in range(len(check)):
            check[i] = check[i][1]
        for i in range(len(check)):
            check[i]=sorted(check[i])

            for j in range(len(check[i])):
                check[i][j]=check[i][j][1]

       


        return check
        
        
        
        