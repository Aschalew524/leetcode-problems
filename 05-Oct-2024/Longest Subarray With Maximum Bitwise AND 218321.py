# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

                       
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_=0
        ans=0
        curr=0
        for num in nums:
            if max_<num: 
                max_=num
                ans=curr=0 
            if max_==num:
                curr+=1
            else:
                curr=0
            ans=max(ans,curr)
        return  ans  