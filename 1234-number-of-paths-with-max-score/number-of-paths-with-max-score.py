class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n-1][n-1] = [0, 1]
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or dp[r][c][0] == -1:
                    continue
                    
                current_score, current_paths = dp[r][c]
                
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':
                        cell_val = int(board[nr][nc]) if board[nr][nc] not in ('E', 'S') else 0
                        next_score = current_score + cell_val
                        
                        if next_score > dp[nr][nc][0]:
                            dp[nr][nc] = [next_score, current_paths]
                        elif next_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + current_paths) % MOD
                            
        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]