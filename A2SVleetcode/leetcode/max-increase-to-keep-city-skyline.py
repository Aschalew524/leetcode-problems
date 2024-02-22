class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        largest_R = [max(grid[i]) for i in range(len(grid))]
        largest_C = [0]* len(grid)
        count=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                largest_C[j] = max(largest_C[j], grid[i][j])
    
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] < largest_R[i] and grid[i][j] < largest_C[j]:
                    count += min(largest_R[i],  largest_C[j]) - grid[i][j]

        return count