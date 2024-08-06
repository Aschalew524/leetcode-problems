# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        incoming = [0 for _ in range(n)]
        if n==1 and edges==[]:
            return [0]
        for u, v in edges:
            dic[u].append(v)
            dic[v].append(u)
            incoming[u] += 1
            incoming[v] += 1
        
        queue = deque()
        min_ = []
        
        for i in range(n):
            if incoming[i] == 1:
                queue.append(i)
        
        while queue:
            min_ = list(queue)
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                for neighbor in dic[node]:
                    incoming[neighbor] -= 1
                    if incoming[neighbor] == 1:
                        queue.append(neighbor)
        
        return min_