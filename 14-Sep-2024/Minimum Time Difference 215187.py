# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = set(timePoints)
        if len(times) != len(timePoints):
            return 0
        lis = []
        for time in times:
            hr = int(time[0:2])
            minute = int(time[3:5])
            lis.append(60*hr+minute)
        lis.sort()
        minMinutes = 24*60+lis[0]-lis[-1]
        for i in range(1,len(lis)):
            minMinutes = min(minMinutes,lis[i]-lis[i-1])
        return minMinutes

        