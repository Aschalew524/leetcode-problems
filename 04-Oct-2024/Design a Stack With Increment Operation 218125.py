# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        
        

    def pop(self) -> int:
        if len(self.stack)> 0:
       
            return self.stack.pop() 
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        min_ = min(k,len(self.stack))
        for i in range(min_):
            self.stack[i]+=val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)