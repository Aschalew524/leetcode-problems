# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i,nodes in enumerate(equations):
            u,v=nodes[0],nodes[1]
            graph[u].append((v,values[i]))
            graph[v].append((u,1/values[i]))
        def bfs(source,target):
            if target not in graph or source not in graph:
                return -1
            queue=deque()
            visited=set()
            queue.append([source,1])
            visited.add(source)
            while queue:
                n,w=queue.popleft()
                if n==target:
                    return w
                for neighbour,weight in graph[n]:
                    if neighbour not in visited:
                        queue.append((neighbour,w*weight))
                        visited.add(neighbour)
            return -1
        return [bfs(q[0],q[1]) for q in queries]
            





        