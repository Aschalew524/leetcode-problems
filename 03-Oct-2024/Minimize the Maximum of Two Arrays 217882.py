# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        

        l = 1
        r= 10 ** 10
        lcm = math.lcm(divisor1, divisor2)
        while l <= r:
            mid = l + (r-l) //2 

            if mid - mid // divisor1 < uniqueCnt1 or mid - mid // divisor2 < uniqueCnt2  or  mid - mid//lcm <  uniqueCnt1 +  uniqueCnt2:
                l = mid +1
            else:
                r= mid -1
        return l