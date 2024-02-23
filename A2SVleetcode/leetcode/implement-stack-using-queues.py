class MyStack:
    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        self.s.append(x)
        for i in range(len(self.s)-1):
            self.s.append(self.s.pop(0))
        

    def pop(self) -> int:
        return self.s.pop(0)
        

    def top(self) -> int:
        return self.s[0]



    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()