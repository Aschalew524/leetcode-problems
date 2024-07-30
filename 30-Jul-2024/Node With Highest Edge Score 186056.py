# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:

    def edgeScore(self, edges: [int]) -> int:
        scores = {}
        max_ = 0

        for i in range(len(edges)):
            if edges[i] not in scores:
                scores[edges[i]] = 0
            scores[edges[i]] += i

            if scores[edges[i]] > max_:
                max_ = scores[edges[i]]

        max_nodes = []
        for node in scores:
            if scores[node] == max_:
                max_nodes.append(node)

        return min(max_nodes)