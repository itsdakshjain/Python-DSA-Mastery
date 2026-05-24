class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = [-1] * n
        
        def dfs(i: int) -> int:
            if memo[i] != -1:
                return memo[i]
            
            max_visited = 1
            
            for x in range(1, d + 1):
                j = i + x
                if j >= n or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            for x in range(1, d + 1):
                j = i - x
                if j < 0 or arr[j] >= arr[i]:
                    break
                max_visited = max(max_visited, 1 + dfs(j))
                
            memo[i] = max_visited
            return memo[i]
            
        return max(dfs(i) for i in range(n))