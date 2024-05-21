# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

from collections import defaultdict, deque

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        incoming = [0] * n
        graph = defaultdict(list)
        queue = deque()
        ans = [i for i in range(n)]
        for u, v in richer:
            graph[u].append(v)
            incoming[v] += 1

        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if quiet[neighbor] > quiet[node]:
                    quiet[neighbor] = quiet[node]
                    ans[neighbor] = ans[node]
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                

        return ans