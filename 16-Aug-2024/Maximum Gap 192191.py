# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        lis = sorted(nums)
        arr = []
        for i in range(1,len(lis)):
            arr.append(lis[i]-lis[i-1])
        return max(arr)