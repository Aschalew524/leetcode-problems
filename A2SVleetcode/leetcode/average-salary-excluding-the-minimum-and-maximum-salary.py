class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        summ=0
        for i in range(1,len(salary)-1):
            summ+=salary[i]
            
        return (summ/(len(salary)-2))
        