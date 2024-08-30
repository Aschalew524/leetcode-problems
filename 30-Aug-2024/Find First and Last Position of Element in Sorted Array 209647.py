# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
     
        def bsf(nums):
         
            left=0
            right=len(nums)-1
            first_target=-1
            
           
            while left <= right:
                mid=(left+ right)//2
                if nums[mid]==target:
                    first_target=mid
                    right=mid-1
                    
                    
                elif nums[mid] < target:
                    left=mid+1
                    
                else:
                    right=mid-1
            return  first_target
        def bs(nums):
           
            left=0
            right=len(nums)-1
            second_target=-1
          
            while left <= right:
                mid=(left+right)//2
                if nums[mid]==target:
                    second_target=mid
                    left=mid+1
                    
                    
                elif nums[mid] < target:
                    left=mid+1
                    
                    
                else:
                    right=mid-1
            return second_target
        first = bsf(nums)
        last= bs(nums)
        return [first,last]
            
                
                    

        