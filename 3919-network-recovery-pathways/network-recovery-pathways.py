class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            in_degree[v] += 1
            
        topo_order = []
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        unique_costs = sorted(list(set(cost for _, _, cost in edges)))
        
        def isValid(min_cost_threshold):
            dist = [float('inf')] * n
            dist[0] = 0
            
            for u in topo_order:
                if dist[u] == float('inf'):
                    continue
                if u != 0 and not online[u]:
                    continue
                for v, cost in adj[u]:
                    if cost >= min_cost_threshold:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
            return dist[n - 1] <= k

        if not isValid(-1):
            return -1
            
        low = 0
        high = len(unique_costs) - 1
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if isValid(unique_costs[mid]):
                ans = unique_costs[mid]
                low = mid + 1
            else:
                high = mid - 1
                
        return ans
