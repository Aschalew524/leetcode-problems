# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution(object):
    def findCenter(self, edges):
        degree=[0]*(len(edges)+2)
        for u,v in edges:
            degree[u]+=1
            degree[v]+=1
        max_=0
        for i in range(len(degree)):
            if max_ < degree[i]:
                max_= i
        return max_
            
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        