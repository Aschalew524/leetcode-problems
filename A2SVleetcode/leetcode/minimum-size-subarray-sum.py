class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            right=0
            left=0
            minn=float("inf")
            summ=0
            while right < len(nums):
                summ += nums[right]
    
                while summ >= target:
                    minn = min(minn, right - left + 1)
                    summ -= nums[left]
                    left += 1
    
                right += 1


            if minn == float("inf"):
                minn = 0

            
            return minn