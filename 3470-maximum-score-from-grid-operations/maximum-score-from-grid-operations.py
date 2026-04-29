class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        prefix = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                prefix[j][i + 1] = prefix[j][i] + grid[i][j]

        prev_pick = [0] * (n + 1)
        prev_skip = [0] * (n + 1)

        for j in range(1, n):
            curr_pick = [0] * (n + 1)
            curr_skip = [0] * (n + 1)
            max_val = -float('inf')
            for k in range(n + 1):
                max_val = max(max_val, prev_skip[k] - prefix[j - 1][k])
                curr_pick[k] = max(curr_pick[k], max_val + prefix[j - 1][k])
                curr_skip[k] = max(curr_skip[k], max_val + prefix[j - 1][k])

            max_val_pick = -float('inf')
            max_val_skip = -float('inf')
            for k in range(n, -1, -1):
                max_val_pick = max(max_val_pick, prev_pick[k] + prefix[j][k])
                max_val_skip = max(max_val_skip, prev_pick[k])
                curr_pick[k] = max(curr_pick[k], max_val_pick - prefix[j][k])
                curr_skip[k] = max(curr_skip[k], max_val_skip)

            prev_pick = curr_pick
            prev_skip = curr_skip

        return max(prev_pick)