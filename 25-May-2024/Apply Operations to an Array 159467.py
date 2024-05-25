# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l=0
        r=1
        n=len(nums)
        while r < len(nums):
            if nums[r]==nums[l]:
                nums[l]*=2
                nums[r]=0
            l=r
            r+=1
        nums=[nums[i] for i in range(len(nums))if nums[i] != 0]
        dif= n - len(nums)
        nums=nums + [0]*dif
        return nums
        

        
            


        