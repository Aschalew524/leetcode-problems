# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        dic = defaultdict(set)

        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        for i in range(n):
            heap = [[0, i]]
            visited = set()

            while heap:
                dist, node = heappop(heap)
                dic[i].add(node)

                visited.add(node)
                for child, w in graph[node]:
                    if child not in visited and dist + w <= distanceThreshold:
                        heappush(heap, [dist + w, child])
        
        min_ = float('inf')
        idx = 0
        for i in range(n):
            if len(dic[i]) <= min_:
                min_ = len(dic[i])
                idx = i
        return idx