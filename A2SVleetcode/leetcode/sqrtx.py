class Solution:
    def mySqrt(self, x: int) -> int:
       
        if x == 0:
            return 0
        if x == 1:
            return 1
        
    
        left = 1
        right = x
        
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
       
        return right