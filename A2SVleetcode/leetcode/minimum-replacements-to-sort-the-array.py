class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<=nums[i+1]:
                continue
            no_of_operations=ceil(nums[i]/nums[i+1])
            count+=no_of_operations-1
            nums[i]=nums[i]//no_of_operations
        return count

        
    