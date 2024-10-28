# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append((edges[i][1],succProb[i]))
            graph[edges[i][1]].append((edges[i][0],succProb[i]))
        
        def dijkstra(src,dst):
            heap = [(-1,src)]
            processed = set()
            while heap:
                cost,node = heapq.heappop(heap)
                if node == dst:
                    return - cost
                if node in processed:
                    continue
                processed.add(node)
                for nei,cost_2 in graph[node]:
                    if nei not in processed:
                        heapq.heappush(heap,((cost * cost_2),nei))
            return 0
        return dijkstra(start_node,end_node)