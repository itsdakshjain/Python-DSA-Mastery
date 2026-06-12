class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        MOD = 10**9 + 7
        LOG = 18
        depth = [0] * (n + 1)
        up = [[0] * LOG for _ in range(n + 1)]
        
        parent = {1: 0}
        order = []
        queue = [1]
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            order.append(curr)
            for neighbor in adj[curr]:
                if neighbor != parent[curr]:
                    parent[neighbor] = curr
                    depth[neighbor] = depth[curr] + 1
                    queue.append(neighbor)
                    
        for node in order:
            p = parent[node]
            up[node][0] = p
            for j in range(1, LOG):
                up[node][j] = up[up[node][j-1]][j-1]
                
        def get_dist(u, v):
            orig_u, orig_v = u, v
            if depth[u] < depth[v]:
                u, v = v, u
            
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
            
            if u == v:
                return depth[orig_u] + depth[orig_v] - 2 * depth[u]
                
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            
            lca = up[u][0]
            return depth[orig_u] + depth[orig_v] - 2 * depth[lca]

        max_len = n + 5
        pow2 = [1] * max_len
        for i in range(1, max_len):
            pow2[i] = (pow2[i-1] * 2) % MOD
            
        ans = []
        for u, v in queries:
            k = get_dist(u, v)
            if k == 0:
                ans.append(0)
            else:
                ans.append(pow2[k - 1])
                
        return ans