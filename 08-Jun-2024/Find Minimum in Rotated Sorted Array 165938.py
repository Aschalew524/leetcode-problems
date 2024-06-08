# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums):
        l=0
        r=len(nums)-1
        min_=nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                min_=min(nums[l],min_)
                break

            m=(l+r)//2
            min_=min(nums[m],min_)
            if nums[m] >= nums[r]:
                l=m+1
            else:
                r=m-1
        return min_
                
               

           


            
        