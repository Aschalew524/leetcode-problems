# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1

        indegree = [0 for _ in range(n)]

        for u in range(len(edges)):
            if edges[u] == -1:
                continue
            indegree[edges[u]] += 1
        
        for u in range(n):
            while indegree[u] == 0 and edges[u] != -1:
                v = edges[u]
                edges[u] = -1
                indegree[v] -= 1
                u = v

        visited = set()

        for u in range(n):
            if indegree[u] == 0 or u in visited:
                continue
            dis = 1
            visited.add(u)

            while edges[u] not in visited:
                v = edges[u]
                dis += 1
                u = v

            ans = max(ans, dis)
        return ans

            

        