# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UF:
    def __init__(self, n):
        self.root = list(range(n))
    
    def find(self, x, y):
        rootX = self.union(x)
        rootY = self.union(y)
        if rootX != rootY:
          
            self.root[rootY] = rootX
            return True
        return False
    
    def union(self, idx):
        if self.root[idx] == idx:
            return idx
        self.root[idx] = self.union(self.root[idx])
        return self.root[idx]

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        ufA, ufB, ufAB = UF(n), UF(n), UF(n)
        usefulAB = 0
        for e in edges:
            if e[0] == 1:
                ufA.find(e[1] - 1, e[2] - 1)
            elif e[0] == 2:
                ufB.find(e[1] - 1, e[2] - 1)
            else:
                ufA.find(e[1] - 1, e[2] - 1)
                ufB.find(e[1] - 1, e[2] - 1)
                usefulAB += ufAB.find(e[1] - 1, e[2] - 1)
        if len([i for i in range(n) if ufA.root[i] == i]) > 1 or len([i for i in range(n) if ufB.root[i] == i]) > 1 :
            return -1
        return len(edges) - (n - 1) * 2 + usefulAB