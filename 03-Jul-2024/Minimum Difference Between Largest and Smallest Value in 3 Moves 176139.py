# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution(object):
    def minDifference(self, nums):
        n=len(nums)
        lis = sorted(nums)
        
        if n <= 4:
            return 0
        if n==5:
           return  min(lis[i]-lis[i-1] for i in range(1,n))
        else:
            return min(lis[-4] - lis[0],lis[-1]-lis[3],lis[-2] - lis[2], lis[-3] - lis[1])
        """
        :type lis: List[int]
        :rtype: int
        """
        