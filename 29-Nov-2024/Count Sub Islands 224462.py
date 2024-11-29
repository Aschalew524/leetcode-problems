# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m, n = len(grid2), len(grid2[0])

        def dfs(r, c):
            stack = [(r, c)]
            is_sub_island = True

            while stack:
                x, y = stack.pop()

                if x < 0 or y < 0 or x >= m or y >= n or grid2[x][y] == 0:
                    continue

                if grid1[x][y] == 0:
                    is_sub_island = False

                grid2[x][y] = 0  # Mark as visited

                stack.append((x - 1, y))  
                stack.append((x + 1, y)) 
                stack.append((x, y - 1))  
                stack.append((x, y + 1))  

            return is_sub_island

        count = 0


        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        ans += 1
        return ans


