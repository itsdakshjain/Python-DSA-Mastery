class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dp = [[{} for _ in range(n)] for _ in range(m)]
        
        start_val = grid[0][0]
        start_score = start_val
        start_cost = 1 if start_val > 0 else 0
        
        if start_cost <= k:
            dp[0][0][start_cost] = start_score
        else:
            return -1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                cell_score = val
                cell_cost = 1 if val > 0 else 0
                
                sources = []
                if i > 0: sources.append(dp[i-1][j])
                if j > 0: sources.append(dp[i][j-1])
                
                for source_dp in sources:
                    for prev_cost, prev_score in source_dp.items():
                        new_cost = prev_cost + cell_cost
                        if new_cost <= k:
                            new_score = prev_score + cell_score
                            if new_score > dp[i][j].get(new_cost, -1):
                                dp[i][j][new_cost] = new_score
                                
        if not dp[m-1][n-1]:
            return -1
            
        return max(dp[m-1][n-1].values())    