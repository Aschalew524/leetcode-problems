# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, graph, color):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    if color[node] == 0:
                        color[neighbour] = 1
                    else:
                        color[neighbour] = 0
                    if not dfs(neighbour, graph, color):
                        return False
                elif color[neighbour] == color[node]:
                    return False
            return True

        n = len(graph)
        color = [-1] * n  
        result = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0 
                result = result and dfs(node, graph, color)
                if not result:  
                    return False
        return result