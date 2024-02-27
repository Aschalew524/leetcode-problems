class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost= sorted(costs, key=lambda x: x[0]-x[1])
        summ=0
        midd=int(len(costs)/2)
        for i in range(midd):
            summ+=cost[i][0]
        for i in range(midd,len(costs)):
            summ+=cost[i][1]

        return(summ)