class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        max_=0
        def check(m):
            curr=0
            for i in range(len(nums)):
                curr+= math.ceil(nums[i]/m)
                
            if curr <= threshold:
                return True
            return False


            
        while l < r:
            m=(l+r)//2
            if check(m):
                r=m
                
            else:
               l=m+1 
        return l




        