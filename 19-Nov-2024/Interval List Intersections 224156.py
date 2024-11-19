# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        M, N = len(firstList), len(secondList)
        i, j = 0, 0

        while i < M and j < N:
            l1, r1 = firstList[i][0], firstList[i][1]
            l2, r2 = secondList[j][0], secondList[j][1]

            l = max(l1, l2)
            r = min(r1, r2)

            if l <= r:
                ans.append([l, r])
            
            if r1 < r2:
                i += 1
            else:
                j += 1
        
        return ans