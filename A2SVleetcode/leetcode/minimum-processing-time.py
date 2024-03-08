class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        lis = []
        processorTime.sort(reverse = True)
        tasks.sort()
        time = len(tasks)//len(processorTime)
        count = 0
        add = 0
        print(processorTime)
        for i in range(len(tasks)):
            if count == time:
                add +=1 
                count =0
            tasks[i]+= processorTime[add] 
            count +=1
        
        return max(tasks)