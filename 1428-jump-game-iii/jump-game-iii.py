class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
            
        queue = deque([start])
        visited = {start}
        n = len(arr)
        
        while queue:
            curr = queue.popleft()
            
            if arr[curr] == 0:
                return True
                
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)
                    
        return False