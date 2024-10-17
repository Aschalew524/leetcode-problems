# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming=[0 for i in range(n+1)]
        for u,v in edges:
            incoming[v]+=1
        ans=[]
        for i in range (n):
            if incoming[i] == 0:
                ans.append(i)
        return ans
        