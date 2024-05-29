# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self,mat):
        n ,m= len(mat), len(mat[0])
        distance = [[float('inf')] * m for _ in range(n)]
        directions= [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(r,c):
            return  0 <= r < n and 0 <=c < m

        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for rc, cc in directions:
                nr, nc = r + rc, c + cc
                if inbound(nr,nc):
                    if distance[nr][nc] > distance[r][c] + 1:
                        distance[nr][nc] = distance[r][c] + 1
                        queue.append((nr, nc))

        return distance