# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s, t):
        check = [0] * 26
        for i in range(len(t)):
            check[ord(t[i])-97]+=1
        for i in range(len(s)):
            check[ord(s[i])-97]-=1
        for i in range(len(check)):
            if check[i] == 1:
                return chr(i+97)