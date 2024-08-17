# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        Memo={}
        def dp(num):
            if num in Memo:
                return Memo[num]
            max_=float("-inf")
            if num==0:
                return 1
            if num<0:
                return float("-inf")
            for i in range(1,n):
                max_= max(max_,i*dp(num-i))
            Memo[num]=max_
            return max_
        return dp(n)