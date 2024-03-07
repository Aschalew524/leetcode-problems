class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        idx = Counter()
        sub = []

        for i in range(len(intervals)):
            idx[intervals[i][0]] = i
            sub.append(intervals[i][0])
        
        sub.sort()
        ans = [-1] * len(intervals)
        
        for i in range(len(intervals)):
            j = intervals[i][1]
            pos = bisect_left(sub, j)
            if pos < len(ans):
                ans[i] = idx[sub[pos]]

        return ans