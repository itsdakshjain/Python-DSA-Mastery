class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        safeness = [[-1] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    safeness[r][c] = 0
                    queue.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and safeness[nr][nc] == -1:
                    safeness[nr][nc] = safeness[r][c] + 1
                    queue.append((nr, nc))

        max_heap = [(-safeness[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while max_heap:
            safe_factor, r, c = heapq.heappop(max_heap)
            safe_factor = -safe_factor

            if r == n - 1 and c == n - 1:
                return safe_factor

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    next_safe = min(safe_factor, safeness[nr][nc])
                    heapq.heappush(max_heap, (-next_safe, nr, nc))

        return 0