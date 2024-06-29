# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n, edges) :
        graph=defaultdict(list)
        for i,j in edges:
            graph[j].append(i)
        arr=[[] for i in range(n)]
        def dfs(node):            
            visited[node]=1
            for i in graph[node]:
                if visited[i]==0:
                    dfs(i)
                
        
        for i in range(n):
            visited=[0]*n
            dfs(i)
            values=[]
            
            for j in range(n):
                if visited[j]==1:
                    if i!=j:
                        arr[i].append(j)
        
        return arr
   