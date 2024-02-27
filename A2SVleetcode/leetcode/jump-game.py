class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can=0
        for i in range(len(nums)-1):
            can=max(can-1,nums[i])
            if can <=0 and i < len(nums)-1:
                return False            
        return True
                
            

        