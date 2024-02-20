class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        prevEnd = points[0][1]
        arrows = 1

        for start, end in points[1:]:
            if start <= prevEnd:
                prevEnd = min(end, prevEnd)
            else:
                arrows += 1
                prevEnd = end

        return arrows