# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution(object):
    def findMaxFish(self, grid):
        n = len(grid)
        m = len(grid[0])
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        max_ = 0
        visited = set()

        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            cur_sum = grid[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                cur_sum += dfs(nr, nc)
            return cur_sum

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and (i, j) not in visited:
                    max_ = max(max_, dfs(i, j))

        return max_