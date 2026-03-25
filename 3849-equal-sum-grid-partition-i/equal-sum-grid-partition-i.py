class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # 1. Calculate the total sum of all numbers in the grid
        total_sum = sum(sum(row) for row in grid)
        
        # 2. If the total is odd, we can't split it into two equal integers
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # 3. Check for a Horizontal Cut
        current_row_sum = 0
        # We check until m-1 because both sections must be non-empty
        for i in range(len(grid) - 1):
            current_row_sum += sum(grid[i])
            if current_row_sum == target:
                return True
                
        # 4. Check for a Vertical Cut
        current_col_sum = 0
        # We sum up columns one by one
        for j in range(len(grid[0]) - 1):
            for i in range(len(grid)):
                current_col_sum += grid[i][j]
            if current_col_sum == target:
                return True
                
        return False