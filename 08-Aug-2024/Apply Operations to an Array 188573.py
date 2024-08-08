# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left=0
        right=1
        n=len(nums)
        while right < len(nums):
            if nums[right]==nums[left]:
                nums[left]*=2
                nums[right]=0
            left=right
            right+=1
        nums=[nums[i] for i in range(len(nums))if nums[i] != 0]
        dif= n - len(nums)
        nums=nums + [0]*dif
        return nums
        

        
            


        