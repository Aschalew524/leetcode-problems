class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        cnt = Counter()  
        for i in s:
            if i == "(":
                cnt["("] += 1
            elif i == ")" and cnt["("] > 0:
                cnt["("] -= 1
            elif i == ")":
                count += 1
        return cnt["("] + count








            


        
        