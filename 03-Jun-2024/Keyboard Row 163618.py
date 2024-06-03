# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        row1 = "qwertyuiop"
        row2= "asdfghjkl"
        row3="zxcvbnm"
        row1+=row1.upper()
        row2+=row2.upper()
        row3+=row3.upper()
        ans=[]
        for word in words:
            if all(s in row1 for s in word) or all(s in row2 for s in word) or all(s in row3 for s in word):
                ans.append(word)
        return ans

        

        """
        :type words: List[str]
        :rtype: List[str]
        """
        