# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        queue = deque()
        if grid[0][0] == 0:
            queue.append([0, 0])
            visited = set()
            visited.add((0, 0))
        else:
            return -1
        length = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                if (r, c) == (n - 1, m - 1):
                    return length
                for row_change, col_change in directions:
                    new_row = r + row_change
                    new_col = c + col_change
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append([new_row, new_col])
                        visited.add((new_row, new_col))
            length += 1
        return -1