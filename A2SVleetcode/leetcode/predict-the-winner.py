class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def helper(lis):

            if len(lis) == 0:
                return 0
            a = lis[0] - helper(lis[1:])
            b=lis[-1]-helper(lis[:-1])
            
            return max(a,b)
        x=helper(nums)
        
        if x>=0:
            return True
        return False

        
        