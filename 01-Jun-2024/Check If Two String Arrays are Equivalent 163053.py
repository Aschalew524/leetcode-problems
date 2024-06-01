# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s=""
        t=""
        for i in word1:
            s+=i
        for j in word2:
            t+=j
        
        return s == t
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        