class Solution:
     def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]

        dist[0][0] = grid[0][0]
        q = deque([(0, 0)])

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                break

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    weight = grid[nr][nc]
                    if dist[r][c] + weight < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + weight
                        if weight == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))

        return health - dist[m - 1][n - 1] >= 1