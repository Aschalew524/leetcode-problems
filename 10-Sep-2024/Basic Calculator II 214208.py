# Problem: Basic Calculator II - https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        op = "+"
        if not s:
            return 0
        operators = ['+','-','*',"/"]
        nums = set(str(x) for x in range(10))
        for i in range(0,len(s)):
            ch = s[i]
            if ch in nums:
                
                curr = curr*10+int(ch)
            if ch in operators or i == len(s)-1:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '/':
                    stack[-1] = int(stack[-1]/curr)
                elif op =="*":
                    stack[-1] *= curr

                curr = 0
                op = ch
                    
        return sum(stack)