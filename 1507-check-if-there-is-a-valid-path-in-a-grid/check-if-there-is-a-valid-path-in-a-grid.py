class Solution:
    def hasValidPath(self, grid: list[list[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        moves = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            if r == R - 1 and c == C - 1:
                return True
            
            for dr, dc in moves[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:
                    if (-dr, -dc) in moves[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        return False