# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed = set(allowed)  
        
        for word in words: 
            word = set(word)  
            flag = True
            for ch in word:
                if ch not in allowed:  
                    flag = False
                    break
            ans += flag  
        
        return ans