# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in range(len(ops)):
            if ops[i]=="C":
                if stack:
                    stack.pop()
            elif ops[i]=="D":
                if stack:
                    stack.append(stack[-1]*2)
            elif ops[i] == "+":
                    if len(stack) >= 2:
                        stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(ops[i]))
        return sum(stack)


            
                