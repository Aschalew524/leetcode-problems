# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums, limit) :
        min_q=deque()
        max_q=deque()
        max_count=0
        l=0
        for r in range(len(nums)):
            while min_q and min_q[-1]< nums[r]:
                min_q.pop()
            min_q.append(nums[r])
            while max_q and max_q[-1]>nums[r]:
                max_q.pop()
            max_q.append(nums[r])
            while min_q[0]-max_q[0]> limit:
                if min_q[0]==nums[l]:
                    min_q.popleft()
                if max_q[0]==nums[l]:
                    max_q.popleft()
                l+=1
            max_count=max(max_count,r-l + 1)
        return max_count
    
        

        
        
        