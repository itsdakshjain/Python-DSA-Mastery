class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        queue = deque([(0, 0)]) 
        visited = {0}
        
        while queue:
            idx, steps = queue.popleft()
            
            if idx == n - 1:
                return steps

            for neighbor in (idx - 1, idx + 1):
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
            
            if arr[idx] in graph:
                for same_val_idx in graph[arr[idx]]:
                    if same_val_idx not in visited:
                        visited.add(same_val_idx)
                        queue.append((same_val_idx, steps + 1))
                del graph[arr[idx]] 
                
        return -1