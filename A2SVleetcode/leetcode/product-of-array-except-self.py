from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = 1
        answer = [0] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-1, -1, -1):
            answer[i] = prefix[i] * suffix
            suffix *= nums[i]
        
        return answer