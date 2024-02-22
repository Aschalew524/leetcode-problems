class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        hashh={"+":operator.add,"-":operator.sub,"*":operator.mul, "/":operator.truediv }
        operators="-+/*"
        for token in tokens:
            if token in operators:
                b=stack.pop()
                a=stack.pop()
              
                c=hashh[token](a,b)
             
                stack.append(int(c))
            else:
                stack.append(int(token))
       
            
        return stack[-1]
            

        