class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:  

        count= 0 
        for i in range(len(nums)): 
            for e in range(i+1, len(nums)): 
                if nums[i] == nums[e] and i*e % k == 0:
                    count+= 1
        return count