class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        complete_components = 0
        
        for i in range(n):
            if not visited[i]:
                component = []
                queue = [i]
                visited[i] = True
                
                while queue:
                    curr = queue.pop(0)
                    component.append(curr)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                num_vertices = len(component)
                is_complete = True
                for node in component:
                    if len(adj[node]) != num_vertices - 1:
                        is_complete = False
                        break
                
                if is_complete:
                    complete_components += 1
                    
        return complete_components