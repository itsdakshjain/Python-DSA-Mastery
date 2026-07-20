class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        

        flat = [grid[r][c] for r in range(m) for c in range(n)]
        
    
        shifted = flat[-k:] + flat[:-k]
        
        return [shifted[i * n : (i + 1) * n] for i in range(m)]