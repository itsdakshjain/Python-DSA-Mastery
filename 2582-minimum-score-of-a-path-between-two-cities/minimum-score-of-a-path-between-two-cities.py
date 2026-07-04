class Solution:
     def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        min_score = float('inf')
        queue = deque([1])
        visited = {1}
        
        while queue:
            node = queue.popleft()
            for neighbor, weight in adj[node]:
                min_score = min(min_score, weight)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score