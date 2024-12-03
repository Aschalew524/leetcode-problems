# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans=[1]
        
        p2,p3,p5=0,0,0
        
        for i in range(n+1):
            t2=ans[p2]*2
            t3=ans[p3]*3
            t5=ans[p5]*5
            
            temp=min(t2,t3,t5)
            
            ans.append(temp)
            
            if temp==ans[p2]*2:
                p2+=1
            if temp==ans[p3]*3:
                p3+=1
            if temp==ans[p5]*5:
                p5+=1
        return ans[n-1]
        