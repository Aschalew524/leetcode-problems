# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()
        components=[]
        def dfs(node,connected):
            visited.add(node)
            connected.append(node)
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,connected)
        for node in range(n):
            connected=[]
            if node not in visited:
                dfs(node,connected)
                components.append(connected)
        print(components)
        ans = 0
        
        
        for comp in components:
            ans += len(comp) * (n - len(comp))
            n -= len(comp)
            
        return ans 

        
        



        