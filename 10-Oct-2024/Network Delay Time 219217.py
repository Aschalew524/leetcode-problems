# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u, v, w in times:
            if u != v:
                graph[u].append((v, w))

        heap = [(0, k)]
        distances = {}

        while heap:
            time_taken, node = heapq.heappop(heap)

            if node in distances:
                continue
                
            distances[node] = time_taken

            for neighbor, time in graph[node]:
                if neighbor not in distances:
                    new_time = time_taken + time
                    heapq.heappush(heap, (new_time, neighbor))

        if len(distances) != n:
            return -1

        return max(distances.values())