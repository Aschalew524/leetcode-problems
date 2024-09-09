# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        paths = defaultdict(list)
        
        for r1, r2 in redEdges:
            paths[r1].append((r2, 'r'))
        
        for b1, b2 in blueEdges:
            paths[b1].append((b2, 'b'))
        
        q = deque([(0, 0, '')]) 
        visited = set()
        
        while q:
            node, dist, color = q.popleft()
            
            if (node, color) in visited:  
                continue
            
            visited.add((node, color))
            
            if ans[node] == -1:
                ans[node] = dist
            
            for next_node, next_color in paths[node]:
                if color != next_color: 
                    q.append((next_node, dist + 1, next_color))
        
        return ans
            