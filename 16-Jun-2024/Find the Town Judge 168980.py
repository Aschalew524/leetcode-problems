# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n, trust) :
        incoming = defaultdict(int)
        outdegree = defaultdict(int)
        if n == 1:
            return 1
        for i, j in trust:
            incoming[j] += 1
            outdegree[i] += 1

        for node, in_degree in incoming.items():
            if in_degree == n - 1 and outdegree[node] == 0:
                return node

        return -1

       
