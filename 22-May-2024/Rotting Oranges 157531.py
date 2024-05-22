# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        fresh=0
        time=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for rc, cc in directions:
                    new_r = r + rc
                    new_c = c + cc
                    if not inbound(new_r,new_c) or grid[new_r][new_c] != 1:
                        continue
                    else:

                        grid[new_r][new_c]=2
                        queue.append([new_r,new_c])
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                    
            


    
       
            
        
            

        