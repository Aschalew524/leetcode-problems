# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def bs(nums):
            l=0
            r=len(nums)-1
            ans=-1
            while l < r:
                m=(l+r)//2
                count = sum(1 for num in nums if num <= m)
            
                if count > m:
                    r = m  
                else:
                    l = m + 1  
                
            return l  
        return bs(nums)