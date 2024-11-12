# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution(object):
    def getLucky(self, s, k):
        ans = ''
        for c in s:
            ans += str(ord(c) - ord('a') + 1)
        
        while k > 0:
            temp = 0
            for x in ans:
                temp += int(x)  
            ans = str(temp)  
            k -= 1
        return int(ans)  