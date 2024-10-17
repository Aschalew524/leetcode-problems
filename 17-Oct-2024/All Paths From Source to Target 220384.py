# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        def dfs(start,path,ans):
            if start==n-1:
                ans.append(path)
            for i in graph[start]:
                dfs(i, path+[i],ans)
            return ans
        
        return dfs(0,[0],[])
       
        