# Problem: Ugly Number - https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        d=2
        ans=[]
        while d*d <= n:
            while n%d==0:
                ans.append(d)
                n//=d
            d+=1
        if n > 1:
            ans.append(n)
        for num in ans:
            if num not in [2,3,5]:
                return False
        return True


        