class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum=[]
        total=0
        for i in nums:
            total+=i
            self.prefixsum.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        rightsum=self.prefixsum[right]
        if left >0:
            leftsum= self.prefixsum[left-1]
        else:
            leftsum=0
        summ=rightsum-leftsum
        return summ


        
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)