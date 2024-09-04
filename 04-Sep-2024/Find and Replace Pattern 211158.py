# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        def solve(s,p):
            cnt_1= {}
            cnt_2 ={}
            for a,b in zip(s,p):
                if a not in cnt_1: cnt_1[a]=b
                if b not in cnt_2: cnt_2[b]=a

                if a != cnt_2[b] or b != cnt_1[a]: 
                    return False
            return True
        
        for word in words:
            if solve(word, pattern):
                ans.append(word)
        return ans