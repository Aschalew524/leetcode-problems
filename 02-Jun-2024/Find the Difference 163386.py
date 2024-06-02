# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        lst = [0] * 26
        for i in range(len(t)):
            lst[ord(t[i])-97]+=1
        for i in range(len(s)):
            lst[ord(s[i])-97]-=1
        for i in range(len(lst)):
            if lst[i] == 1:
                return chr(i+97)