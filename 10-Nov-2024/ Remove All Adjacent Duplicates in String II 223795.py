# Problem:  Remove All Adjacent Duplicates in String II - https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for i in s:
            if stk and i == stk[-1][0]:
                stk[-1][1] += 1
                if stk[-1][1] >= k:
                    stk.pop()
            else:
                stk.append([i, 1])
        
        ans = ""
        for char, n in stk:
            ans += char * n
        
        return ans